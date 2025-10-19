#!/usr/bin/env python3
"""
freee API Session Management Module

Provides OAuth 2.0 authentication and session management for freee accounting API.
Implements PKCE flow, automatic token storage/refresh, and HTTP request methods.

This module is designed to be executed by Claude Code skill. The FreeeSession class
handles all authentication complexity, allowing Claude to focus on API operations.

Key Features:
- OAuth 2.0 with PKCE authentication flow
- Automatic token persistence (~/.config/freee-skill/tokens.json)
- Automatic token refresh on expiration
- Session-based API requests (GET, POST, PUT, DELETE)
- Configuration management (~/.config/freee-skill/config.json)

Usage:
    from skill.scripts.freee_session import FreeeSession

    # Initialize session (auto-loads tokens if available)
    session = FreeeSession()

    # Authenticate (only needed on first run or after logout)
    session.authenticate()

    # Make API requests
    user = session.get('/api/1/users/me')
    companies = session.get('/api/1/companies')

    # Tokens persist automatically - no need to re-authenticate next time

Dependencies:
    Python 3.7+ standard library only (no external packages required)
"""

import http.server
import json
import hashlib
import secrets
import webbrowser
import threading
import time
from pathlib import Path
from typing import Any, Dict, Optional
from urllib.parse import urlencode, urlparse, parse_qs
from urllib.request import Request, urlopen
from urllib.error import HTTPError


class FreeeSessionError(Exception):
    """FreeeSession のエラー基底クラス"""
    pass


class AuthenticationError(FreeeSessionError):
    """認証関連のエラー"""
    pass


class TokenRefreshError(FreeeSessionError):
    """トークンリフレッシュのエラー"""
    pass


class APIError(FreeeSessionError):
    """API 呼び出しのエラー"""
    def __init__(self, message: str, status_code: Optional[int] = None, response_data: Optional[Dict] = None):
        super().__init__(message)
        self.status_code = status_code
        self.response_data = response_data


class _ConfigManager:
    """設定ファイルの管理"""

    DEFAULT_CONFIG_DIR = Path.home() / '.config' / 'freee-skill'
    DEFAULT_CONFIG_FILE = DEFAULT_CONFIG_DIR / 'config.json'

    DEFAULT_CONFIG = {
        'client_id': '',
        'client_secret': '',
        'callback_port': 8080,
        'api_url': 'https://api.freee.co.jp',
        'authorization_endpoint': 'https://accounts.secure.freee.co.jp/public_api/authorize',
        'token_endpoint': 'https://accounts.secure.freee.co.jp/public_api/token',
        'scope': 'read write',
        'auth_timeout_seconds': 300,
    }

    def __init__(self, config_path: Optional[Path] = None):
        self.config_path = config_path or self.DEFAULT_CONFIG_FILE
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """設定ファイルを読み込む"""
        if not self.config_path.exists():
            # 設定ファイルが存在しない場合、自動作成
            self._create_default_config()
            return self.DEFAULT_CONFIG.copy()

        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                user_config = json.load(f)

            # デフォルト値とマージ
            config = self.DEFAULT_CONFIG.copy()
            config.update(user_config)
            return config
        except Exception as e:
            print(f"設定ファイルの読み込みエラー: {e}")
            return self.DEFAULT_CONFIG.copy()

    def _create_default_config(self) -> None:
        """デフォルト設定ファイルを作成し、編集を促す"""
        self.config_path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)

        # テンプレートファイルのパスを取得（スクリプトと同じディレクトリ）
        template_path = Path(__file__).parent / 'config.json.example'

        # テンプレートファイルが存在する場合はそれを使用
        if template_path.exists():
            try:
                with open(template_path, 'r', encoding='utf-8') as f:
                    template_config = json.load(f)

                with open(self.config_path, 'w', encoding='utf-8') as f:
                    json.dump(template_config, f, indent=2, ensure_ascii=False)

                print(f"\n[CONFIG SETUP REQUIRED]")
                print(f"Configuration file created from template at: {self.config_path}")
            except Exception as e:
                # テンプレート読み込みに失敗した場合はデフォルト値を使用
                print(f"Warning: Failed to load template ({e}). Using default values.")
                with open(self.config_path, 'w', encoding='utf-8') as f:
                    json.dump(self.DEFAULT_CONFIG, f, indent=2, ensure_ascii=False)

                print("\n[CONFIG SETUP REQUIRED]")
                print(f"Configuration file created at: {self.config_path}")
        else:
            # テンプレートが存在しない場合はデフォルト値を使用
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(self.DEFAULT_CONFIG, f, indent=2, ensure_ascii=False)

            print("\n[CONFIG SETUP REQUIRED]")
            print(f"Configuration file created at: {self.config_path}")

        self.config_path.chmod(0o600)

        print("\nPlease edit the configuration file and set:")
        print("  - client_id: Your freee OAuth Client ID")
        print("  - client_secret: Your freee OAuth Client Secret")
        print("\nGet credentials from: https://developer.freee.co.jp/")
        print()

    def ensure_config_valid(self) -> bool:
        """設定が有効かチェックし、無効な場合は設定ファイルパスを表示"""
        if not self.validate():
            print("\n[CONFIGURATION ERROR]")
            print(f"Configuration file is incomplete: {self.config_path}")
            print("\nRequired fields:")
            print("  - client_id")
            print("  - client_secret")
            print("\nExample configuration:")
            print('{')
            print('  "client_id": "your_client_id_here",')
            print('  "client_secret": "your_client_secret_here",')
            print('  "callback_port": 8080')
            print('}')
            print()
            return False
        return True

    def get(self, key: str, default: Any = None) -> Any:
        """設定値を取得"""
        return self.config.get(key, default)

    def validate(self) -> bool:
        """設定の検証"""
        if not self.config.get('client_id'):
            print("エラー: client_id が設定されていません")
            return False
        if not self.config.get('client_secret'):
            print("エラー: client_secret が設定されていません")
            return False
        return True


class _TokenManager:
    """トークンの保存・読み込み・管理"""

    DEFAULT_TOKEN_FILE = Path.home() / '.config' / 'freee-skill' / 'tokens.json'

    def __init__(self, token_path: Optional[Path] = None):
        self.token_path = token_path or self.DEFAULT_TOKEN_FILE
        self.tokens: Optional[Dict[str, Any]] = None

    def load(self) -> Optional[Dict[str, Any]]:
        """トークンファイルを読み込む"""
        if not self.token_path.exists():
            return None

        try:
            with open(self.token_path, 'r', encoding='utf-8') as f:
                self.tokens = json.load(f)
            return self.tokens
        except Exception as e:
            print(f"トークンの読み込みエラー: {e}")
            return None

    def save(self, tokens: Dict[str, Any]) -> None:
        """トークンを保存"""
        self.token_path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)

        with open(self.token_path, 'w', encoding='utf-8') as f:
            json.dump(tokens, f, indent=2)

        self.token_path.chmod(0o600)
        self.tokens = tokens
        print(f"トークンを保存しました: {self.token_path}")

    def is_valid(self) -> bool:
        """トークンが有効かチェック"""
        if not self.tokens:
            return False

        expires_at = self.tokens.get('expires_at', 0)
        # 60秒のバッファを持たせる
        return time.time() < (expires_at - 60)

    def get_access_token(self) -> Optional[str]:
        """アクセストークンを取得"""
        if not self.tokens:
            return None
        return self.tokens.get('access_token')

    def get_refresh_token(self) -> Optional[str]:
        """リフレッシュトークンを取得"""
        if not self.tokens:
            return None
        return self.tokens.get('refresh_token')

    def clear(self) -> None:
        """トークンをクリア"""
        if self.token_path.exists():
            self.token_path.unlink()
            print("トークンをクリアしました")
        self.tokens = None


class _OAuthCallbackHandler(http.server.BaseHTTPRequestHandler):
    """OAuth コールバックを処理するHTTPハンドラー"""

    # クラス変数で状態を共有
    auth_code: Optional[str] = None
    auth_state: Optional[str] = None
    auth_error: Optional[str] = None
    expected_state: Optional[str] = None

    def log_message(self, _format, *_args):
        """Suppress log output (intentionally unused parameters for base class compatibility)"""
        pass

    def do_GET(self):
        """GET リクエストの処理"""
        parsed_path = urlparse(self.path)

        if parsed_path.path == '/callback':
            self._handle_callback(parsed_path)
        else:
            self._send_response(404, '<h1>404 Not Found</h1>')

    def _handle_callback(self, parsed_path):
        """OAuth コールバックの処理"""
        params = parse_qs(parsed_path.query)

        # エラーチェック
        if 'error' in params:
            error = params['error'][0]
            error_description = params.get('error_description', [''])[0]
            _OAuthCallbackHandler.auth_error = f"{error}: {error_description}"
            self._send_response(400, f'<h1>認証エラー</h1><p>{error_description}</p>')
            return

        # コードと状態を取得
        code = params.get('code', [None])[0]
        state = params.get('state', [None])[0]

        if not code or not state:
            _OAuthCallbackHandler.auth_error = "コードまたは状態が不足しています"
            self._send_response(400, '<h1>認証エラー</h1><p>パラメータが不足しています</p>')
            return

        # 状態の検証
        if state != _OAuthCallbackHandler.expected_state:
            _OAuthCallbackHandler.auth_error = "状態の検証に失敗しました"
            self._send_response(400, '<h1>認証エラー</h1><p>不正な状態パラメータです</p>')
            return

        # 成功
        _OAuthCallbackHandler.auth_code = code
        _OAuthCallbackHandler.auth_state = state
        self._send_response(200, '<h1>認証完了</h1><p>認証が完了しました。このページを閉じてください。</p>')

    def _send_response(self, status_code: int, html: str):
        """HTTPレスポンスを送信"""
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))


class FreeeSession:
    """
    freee API Session Manager

    Handles OAuth 2.0 authentication and provides HTTP methods for freee API access.
    Automatically manages token storage, loading, and refresh.

    This class is designed to be simple to use from Claude Code skill:
    1. Initialize: session = FreeeSession()
    2. Authenticate (first time only): session.authenticate()
    3. Make API calls: session.get('/api/1/users/me')

    Tokens persist in ~/.config/freee-skill/tokens.json and are automatically
    refreshed when expired. Configuration is stored in ~/.config/freee-skill/config.json.

    Attributes:
        config (_ConfigManager): Configuration file manager
        token_manager (_TokenManager): Token storage and refresh manager

    Example:
        >>> session = FreeeSession()
        >>> session.authenticate()  # Only needed first time
        >>> user = session.get('/api/1/users/me')
        >>> companies = session.get('/api/1/companies')
    """

    def __init__(self, config_path: Optional[Path] = None, token_path: Optional[Path] = None):
        """
        Initialize FreeeSession

        Args:
            config_path: Path to configuration file (default: ~/.config/freee-skill/config.json)
            token_path: Path to token file (default: ~/.config/freee-skill/tokens.json)
        """
        self.config = _ConfigManager(config_path)
        self.token_manager = _TokenManager(token_path)

        # トークンを読み込む
        self.token_manager.load()

        # PKCEパラメータ
        self._code_verifier: Optional[str] = None
        self._code_challenge: Optional[str] = None
        self._state: Optional[str] = None

    def authenticate(self, force: bool = False) -> None:
        """
        OAuth 2.0 認証を実行

        Args:
            force: True の場合、既存のトークンがあっても再認証

        Raises:
            AuthenticationError: 認証に失敗した場合
        """
        # 設定の検証
        if not self.config.ensure_config_valid():
            raise AuthenticationError("Configuration is incomplete. Please edit the config file.")

        # 既存のトークンチェック
        if not force and self.token_manager.load() and self.token_manager.is_valid():
            print("有効なトークンが存在します。")
            return

        # リフレッシュトークンがあれば試す
        if not force and self.token_manager.get_refresh_token():
            try:
                self._refresh_token()
                print("トークンをリフレッシュしました。")
                return
            except TokenRefreshError:
                print("トークンのリフレッシュに失敗しました。再認証します。")

        # PKCE パラメータ生成
        self._generate_pkce()

        # コールバックサーバー起動
        callback_port = self.config.get('callback_port', 8080)
        redirect_uri = f'http://127.0.0.1:{callback_port}/callback'

        server = http.server.HTTPServer(('127.0.0.1', callback_port), _OAuthCallbackHandler)
        server_thread = threading.Thread(target=server.serve_forever, daemon=True)
        server_thread.start()

        print(f"コールバックサーバーを起動しました: {redirect_uri}")

        # 認証URLを生成してブラウザで開く
        auth_url = self._build_auth_url(redirect_uri)
        print(f"ブラウザで認証ページを開きます...")
        print(f"URL: {auth_url}")
        webbrowser.open(auth_url)

        # コールバックを待つ
        timeout = self.config.get('auth_timeout_seconds', 300)
        _OAuthCallbackHandler.expected_state = self._state
        _OAuthCallbackHandler.auth_code = None
        _OAuthCallbackHandler.auth_error = None

        start_time = time.time()
        while time.time() - start_time < timeout:
            if _OAuthCallbackHandler.auth_code:
                break
            if _OAuthCallbackHandler.auth_error:
                server.shutdown()
                raise AuthenticationError(f"認証エラー: {_OAuthCallbackHandler.auth_error}")
            time.sleep(0.5)

        server.shutdown()

        if not _OAuthCallbackHandler.auth_code:
            raise AuthenticationError("認証がタイムアウトしました")

        # トークン取得
        self._exchange_code_for_tokens(_OAuthCallbackHandler.auth_code, redirect_uri)
        print("認証が完了しました！")

    def _generate_pkce(self) -> None:
        """PKCE パラメータを生成"""
        self._code_verifier = secrets.token_urlsafe(32)
        challenge_bytes = hashlib.sha256(self._code_verifier.encode()).digest()
        self._code_challenge = challenge_bytes.hex()
        self._state = secrets.token_urlsafe(32)

    def _build_auth_url(self, redirect_uri: str) -> str:
        """認証URLを構築"""
        params = {
            'response_type': 'code',
            'client_id': self.config.get('client_id'),
            'redirect_uri': redirect_uri,
            'scope': self.config.get('scope'),
            'state': self._state,
            'code_challenge': self._code_challenge,
            'code_challenge_method': 'S256',
        }

        auth_endpoint = self.config.get('authorization_endpoint')
        return f"{auth_endpoint}?{urlencode(params)}"

    def _exchange_code_for_tokens(self, code: str, redirect_uri: str) -> None:
        """認証コードをトークンに交換"""
        token_endpoint = self.config.get('token_endpoint')

        data = {
            'grant_type': 'authorization_code',
            'client_id': self.config.get('client_id'),
            'client_secret': self.config.get('client_secret'),
            'code': code,
            'redirect_uri': redirect_uri,
            'code_verifier': self._code_verifier,
        }

        try:
            response = self._http_request(
                token_endpoint,
                method='POST',
                data=urlencode(data).encode('utf-8'),
                headers={'Content-Type': 'application/x-www-form-urlencoded'}
            )

            token_data = json.loads(response)
            tokens = {
                'access_token': token_data['access_token'],
                'refresh_token': token_data['refresh_token'],
                'expires_at': time.time() + token_data['expires_in'],
                'token_type': token_data.get('token_type', 'Bearer'),
                'scope': token_data.get('scope', self.config.get('scope')),
            }

            self.token_manager.save(tokens)
        except Exception as e:
            raise AuthenticationError(f"トークン取得エラー: {e}")

    def _refresh_token(self) -> None:
        """トークンをリフレッシュ"""
        refresh_token = self.token_manager.get_refresh_token()
        if not refresh_token:
            raise TokenRefreshError("リフレッシュトークンがありません")

        token_endpoint = self.config.get('token_endpoint')

        data = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': self.config.get('client_id'),
            'client_secret': self.config.get('client_secret'),
        }

        try:
            response = self._http_request(
                token_endpoint,
                method='POST',
                data=urlencode(data).encode('utf-8'),
                headers={'Content-Type': 'application/x-www-form-urlencoded'}
            )

            token_data = json.loads(response)
            tokens = {
                'access_token': token_data['access_token'],
                'refresh_token': token_data.get('refresh_token', refresh_token),
                'expires_at': time.time() + token_data['expires_in'],
                'token_type': token_data.get('token_type', 'Bearer'),
                'scope': token_data.get('scope', self.config.get('scope')),
            }

            self.token_manager.save(tokens)
        except Exception as e:
            raise TokenRefreshError(f"トークンリフレッシュエラー: {e}")

    def _ensure_valid_token(self) -> str:
        """有効なアクセストークンを取得（必要ならリフレッシュ）"""
        if not self.token_manager.tokens:
            raise AuthenticationError("認証が必要です。先に authenticate() を実行してください。")

        if not self.token_manager.is_valid():
            print("トークンの有効期限が切れています。リフレッシュします...")
            self._refresh_token()

        access_token = self.token_manager.get_access_token()
        if not access_token:
            raise AuthenticationError("アクセストークンが取得できません")

        return access_token

    def _http_request(self, url: str, method: str = 'GET', data: Optional[bytes] = None,
                     headers: Optional[Dict[str, str]] = None) -> str:
        """HTTP リクエストを実行（内部用）"""
        req_headers = headers or {}

        request = Request(url, data=data, headers=req_headers, method=method)

        try:
            with urlopen(request) as response:
                return response.read().decode('utf-8')
        except HTTPError as e:
            error_body = e.read().decode('utf-8')
            try:
                error_data = json.loads(error_body)
            except:
                error_data = {'error': error_body}

            raise APIError(
                f"HTTP Error {e.code}: {error_data}",
                status_code=e.code,
                response_data=error_data
            )

    def request(self, method: str, path: str, params: Optional[Dict] = None,
               json_data: Optional[Dict] = None, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        freee API にリクエストを送信

        Args:
            method: HTTPメソッド ('GET', 'POST', 'PUT', 'DELETE')
            path: APIパス（例: '/api/1/users/me'）
            params: クエリパラメータ
            json_data: JSONボディ
            headers: 追加のHTTPヘッダー

        Returns:
            APIレスポンス（JSON）

        Raises:
            APIError: APIエラーの場合
        """
        access_token = self._ensure_valid_token()

        # URLを構築
        api_url = self.config.get('api_url')
        url = f"{api_url}{path}"
        if params:
            url = f"{url}?{urlencode(params)}"

        # ヘッダーを構築
        req_headers = {
            'Authorization': f'Bearer {access_token}',
            'Accept': 'application/json',
        }
        if headers:
            req_headers.update(headers)

        # データを準備
        data = None
        if json_data:
            data = json.dumps(json_data).encode('utf-8')
            req_headers['Content-Type'] = 'application/json'

        # リクエスト実行
        response_text = self._http_request(url, method=method, data=data, headers=req_headers)

        # JSONパース
        try:
            return json.loads(response_text)
        except json.JSONDecodeError:
            return {'response': response_text}

    def get(self, path: str, params: Optional[Dict] = None, **kwargs) -> Dict[str, Any]:
        """GET リクエスト"""
        return self.request('GET', path, params=params, **kwargs)

    def post(self, path: str, json_data: Optional[Dict] = None, **kwargs) -> Dict[str, Any]:
        """POST リクエスト"""
        return self.request('POST', path, json_data=json_data, **kwargs)

    def put(self, path: str, json_data: Optional[Dict] = None, **kwargs) -> Dict[str, Any]:
        """PUT リクエスト"""
        return self.request('PUT', path, json_data=json_data, **kwargs)

    def delete(self, path: str, **kwargs) -> Dict[str, Any]:
        """DELETE リクエスト"""
        return self.request('DELETE', path, **kwargs)

    def logout(self) -> None:
        """ログアウト（トークンをクリア）"""
        self.token_manager.clear()
        print("ログアウトしました")


def create_default_config(config_path: Optional[Path] = None) -> None:
    """
    デフォルトの設定ファイルを作成

    Args:
        config_path: 設定ファイルのパス（省略時はデフォルト）
    """
    config_manager = _ConfigManager(config_path)
    config_manager.save_default_config()


if __name__ == '__main__':
    """
    Example usage when running this script directly.
    Demonstrates authentication and basic API calls.
    """
    print("freee API Session - Example Usage")
    print("-" * 50)

    try:
        # Initialize session
        # If config doesn't exist, it will be created with instructions
        session = FreeeSession()

        # Authenticate
        # If config is incomplete, error message with instructions will display
        session.authenticate()

        # Example API calls
        print("\nFetching user information...")
        user_info = session.get('/api/1/users/me')
        print(json.dumps(user_info, indent=2, ensure_ascii=False))

        print("\nFetching companies...")
        companies = session.get('/api/1/companies')
        print(json.dumps(companies, indent=2, ensure_ascii=False))

        print("\n[SUCCESS] Example completed successfully")

    except FreeeSessionError as e:
        print(f"\n[ERROR] {e}")
        print("\nPlease check:")
        print("1. Configuration file: ~/.config/freee-skill/config.json")
        print("2. OAuth credentials are valid")
        print("3. Network connectivity")
