---
name: freee-api-skill
description: "freee 会計・人事労務 API を操作するスキル。OAuth 認証とトークン管理を自動化し、経費申請、会計データ取得、人事情報管理など、freee の様々な機能を Python スクリプトまたは CLI ツールから利用可能。"
---

# freee API スキル

## このスキルについて

Python スクリプトを通じて freee 会計・人事労務 API と直接連携する。OAuth 2.0 (PKCE) による認証、自動トークン管理、セッションベースの API リクエストを提供する。

**主な機能**:

- 経費申請の作成と管理
- 会計データの取得と参照
- 人事労務情報の管理（従業員、勤怠、給与など）
- 請求書・見積書の操作
- 部門、タグなどのマスタ情報の取得
- 事業所情報の管理
- 自動 OAuth トークンリフレッシュ

## 前提条件

このスキルを使用する前に、以下を準備する：

- Python 3.7 以上
- freee 開発者アカウント（Client ID/Secret）
- 対象事業所へのアクセス権限

**OAuth アプリケーションのセットアップ**:
1. https://developer.freee.co.jp/ で OAuth アプリケーションを作成
2. Client ID と Client Secret を取得
3. リダイレクト URI を設定: `http://127.0.0.1:8080/callback`

## 同梱リソース

### スクリプト

**`scripts/freee_session.py`** - freee API アクセス用 Python モジュール

このスクリプトは `FreeeSession` クラスを提供し、以下を処理する:
- OAuth 2.0 (PKCE) 認証フロー
- トークンの自動保存とリフレッシュ（`~/.config/freee-skill/tokens.json` に永続化）
- セッションベースの API リクエスト（GET, POST, PUT, DELETE）
- 設定管理（`~/.config/freee-skill/config.json`）

Python 標準ライブラリのみで動作する（外部依存なし）。

**使用例（Python ライブラリとして）**:
```python
from skill.scripts.freee_session import FreeeSession

# セッション初期化（トークンがあれば自動読み込み）
session = FreeeSession()

# 認証（初回のみ）
session.authenticate()

# API 呼び出し
user = session.get('/api/1/users/me')
companies = session.get('/api/1/companies')
```

**`scripts/freee_api.py`** - freee API CLI ツール

コマンドラインから直接 freee API を呼び出すツール。Claude が外部プロセスとして実行する際や、手動テストに便利。

**使用例（CLI ツールとして）**:
```bash
# ユーザー情報を取得
./skill/scripts/freee_api.py GET /api/1/users/me

# 会社一覧を取得
./skill/scripts/freee_api.py GET /api/1/companies

# クエリパラメータ付き GET
./skill/scripts/freee_api.py GET /api/1/deals \
  -p '{"company_id": 123456, "start_date": "2025-01-01"}'

# POST リクエスト（経費申請の作成）
./skill/scripts/freee_api.py POST /api/1/expense_applications \
  -d '{"company_id": 123456, "title": "交通費", "issue_date": "2025-01-15"}'

# PUT リクエスト（データ更新）
./skill/scripts/freee_api.py PUT /api/1/deals/789 \
  -d '{"memo": "更新しました"}'

# DELETE リクエスト
./skill/scripts/freee_api.py DELETE /api/1/deals/789

# 生 JSON 出力（整形なし）
./skill/scripts/freee_api.py GET /api/1/users/me --raw

# 詳細モード（リクエスト内容を表示）
./skill/scripts/freee_api.py GET /api/1/users/me --verbose
```

**CLI オプション**:
- `-p` / `--params`: クエリパラメータ（JSON 文字列）
- `-d` / `--data`: リクエストボディ（JSON 文字列）
- `--raw`: 生 JSON 出力
- `--verbose` / `-v`: 詳細モード
- `--help` / `-h`: ヘルプ表示

### リファレンス

このスキルには 65+ の API リファレンスファイルが含まれる。必要に応じて読み込み、API の使用方法を確認する。

**人事労務 API** (`references/hr-*.md`)

従業員情報、勤怠管理、給与明細などの人事労務関連 API。

主なリファレンス:
- `hr-employees.md` - 従業員情報の取得・更新
- `hr-attendances.md` - 勤怠情報の取得・登録
- `hr-payroll-statements.md` - 給与明細の取得
- `hr-paid-holiday-requests.md` - 有給休暇申請
- `hr-overtime-requests.md` - 残業申請
- `hr-sections.md` - 部門マスタ

**会計 API** (`references/accounting-*.md`)

取引、請求書、経費精算などの会計関連 API。

主なリファレンス:
- `accounting-deals.md` - 取引の作成・更新
- `accounting-expense-applications.md` - 経費申請の作成・承認
- `accounting-invoices.md` - 請求書の作成・更新
- `accounting-account-items.md` - 勘定科目マスタ
- `accounting-partners.md` - 取引先マスタ
- `accounting-sections.md` - 部門マスタ
- `accounting-companies.md` - 事業所情報

**請求書 API** (`references/invoice-*.md`)

請求書、見積書、納品書の作成・管理。

- `invoice-invoices.md`
- `invoice-quotations.md`
- `invoice-delivery-slips.md`

**プロジェクト管理 API** (`references/pm-*.md`)

- `pm-users.md`

**トラブルシューティング**

- `troubleshooting.md` - よくあるエラーと対処法

**リファレンスの検索方法**:

ファイルが多いため、`grep` を使って必要な情報を検索する:

```bash
# 「従業員」に関する API を探す
grep -l "従業員" skill/references/*.md

# 「勤怠」に関する API を探す
grep -l "勤怠" skill/references/*.md

# 「経費」に関する API を探す
grep -l "経費" skill/references/*.md
```

または Claude の Grep ツールを使用する:

```python
# Grep ツールで references ディレクトリを検索
# pattern: "従業員", path: "skill/references"
```

## 初回セットアップ

### ステップ 1: 設定ファイルの初期化

初回実行時にセッションを初期化すると、設定ファイルが自動作成される:

```python
from skill.scripts.freee_session import FreeeSession

session = FreeeSession()
```

スクリプトは以下を出力する:

```
[CONFIG SETUP REQUIRED]
Configuration file created at: ~/.config/freee-skill/config.json

Please edit the configuration file and set:
  - client_id: Your freee OAuth Client ID
  - client_secret: Your freee OAuth Client Secret

Get credentials from: https://developer.freee.co.jp/
```

### ステップ 2: OAuth 認証情報の設定

`~/.config/freee-skill/config.json` を編集する:

```json
{
  "client_id": "実際の Client ID",
  "client_secret": "実際の Client Secret",
  "callback_port": 8080,
  "api_url": "https://api.freee.co.jp",
  "scope": "read write"
}
```

**設定項目**:
- `client_id`: freee 開発者ポータルの OAuth Client ID
- `client_secret`: freee 開発者ポータルの OAuth Client Secret
- `callback_port`: OAuth コールバックサーバーのポート（デフォルト: 8080）
- `api_url`: freee API のベース URL
- `scope`: 要求する権限スコープ

### ステップ 3: 認証の実行

認証情報を設定後、認証を実行する:

```python
from skill.scripts.freee_session import FreeeSession

session = FreeeSession()
session.authenticate()
```

**認証フロー**:
1. ローカルにコールバックサーバーが起動（ポート 8080）
2. ブラウザが自動で開き、freee ログイン画面が表示される
3. freee アカウントでログイン
4. アクセス許可を承認
5. トークンが `~/.config/freee-skill/tokens.json` に自動保存される

**重要**: 一度認証すれば、トークンは永続化され、有効期限が切れても自動でリフレッシュされる。再認証は不要。

### ステップ 4: セットアップの確認

認証完了後、API を呼び出してセットアップを確認する:

```python
# ユーザー情報を取得
user = session.get('/api/1/users/me')
print(f"ユーザー: {user['user']['display_name']}")

# 利用可能な事業所を取得
companies = session.get('/api/1/companies')
for company in companies['companies']:
    print(f"事業所: {company['display_name']} (ID: {company['id']})")
```

事業所情報が正しく表示されれば、セットアップ完了。

## 使い方

### Python ライブラリとして使用

`FreeeSession` クラスを使って Python コードから API を呼び出す:

```python
from skill.scripts.freee_session import FreeeSession

# セッション作成（トークンは自動読み込み）
session = FreeeSession()

# GET リクエスト: ユーザー情報を取得
user = session.get('/api/1/users/me')
print(user)

# GET リクエスト（パラメータ付き）: 取引を検索
deals = session.get('/api/1/deals', params={
    'company_id': 123456,
    'start_date': '2025-01-01'
})

# POST リクエスト: 経費申請を作成
expense_data = {
    'company_id': 123456,
    'title': '交通費',
    'issue_date': '2025-01-15',
    'description': '取引先訪問の交通費'
}
result = session.post('/api/1/expense_applications', json_data=expense_data)

# PUT リクエスト: データを更新
session.put('/api/1/deals/789', json_data={'memo': '更新しました'})

# DELETE リクエスト: データを削除
session.delete('/api/1/deals/789')
```

### CLI ツールとして使用

`freee_api.py` を使ってコマンドラインから直接 API を呼び出す:

```bash
# 基本的な GET リクエスト
./skill/scripts/freee_api.py GET /api/1/users/me

# パラメータ付き GET
./skill/scripts/freee_api.py GET /api/1/expense_applications \
  -p '{"company_id": 123456}'

# POST リクエスト
./skill/scripts/freee_api.py POST /api/1/expense_applications \
  -d '{
    "company_id": 123456,
    "title": "交通費",
    "issue_date": "2025-01-15",
    "expense_application_lines": [
      {
        "transaction_date": "2025-01-15",
        "description": "交通費",
        "amount": 5000
      }
    ]
  }'

# Python の subprocess から呼び出し
import subprocess
import json

result = subprocess.run([
    './skill/scripts/freee_api.py',
    'GET',
    '/api/1/users/me'
], capture_output=True, text=True, check=True)

user_data = json.loads(result.stdout)
```

### 一般的なワークフロー

**経費申請の作成**

事業所 ID を取得してから経費申請を作成する:

```python
from skill.scripts.freee_session import FreeeSession

session = FreeeSession()

# 事業所 ID を取得
companies = session.get('/api/1/companies')
company_id = companies['companies'][0]['id']

# 経費申請を作成
expense_data = {
    'company_id': company_id,
    'title': '交通費',
    'issue_date': '2025-01-15',
    'expense_application_lines': [
        {
            'transaction_date': '2025-01-15',
            'description': '取引先訪問の交通費',
            'amount': 5000
        }
    ]
}

result = session.post('/api/1/expense_applications', json_data=expense_data)
print(f"経費申請を作成しました: ID {result['expense_application']['id']}")
```

**今月の経費申請を確認**

日付範囲を指定して経費申請を取得する:

```python
from skill.scripts.freee_session import FreeeSession
from datetime import datetime

session = FreeeSession()

# 事業所 ID を取得
companies = session.get('/api/1/companies')
company_id = companies['companies'][0]['id']

# 日付範囲を計算
today = datetime.now()
start_date = today.replace(day=1).strftime('%Y-%m-%d')

# 経費申請を取得
expenses = session.get('/api/1/expense_applications', params={
    'company_id': company_id,
    'start_issue_date': start_date
})

print(f"今月の経費申請: {len(expenses['expense_applications'])} 件")
for exp in expenses['expense_applications']:
    print(f"- {exp['title']}: {exp['total_amount']}円")
```

**部門一覧を取得**

事業所の部門マスタを取得する:

```python
from skill.scripts.freee_session import FreeeSession

session = FreeeSession()

# 事業所 ID を取得
companies = session.get('/api/1/companies')
company_id = companies['companies'][0]['id']

# 部門一覧を取得
sections = session.get('/api/1/sections', params={'company_id': company_id})

print("部門一覧:")
for section in sections['sections']:
    print(f"- {section['name']} (ID: {section['id']})")
```

**従業員情報を取得**

人事労務 API を使って従業員情報を取得する:

```bash
# CLI ツールを使用
./skill/scripts/freee_api.py GET /hr/api/v1/employees \
  -p '{"company_id": 123456}'
```

または Python で:

```python
# まず references/hr-employees.md を読み込んで API 仕様を確認
# その後 API を呼び出す

session = FreeeSession()
employees = session.get('/hr/api/v1/employees', params={
    'company_id': 123456
})
```

### リファレンスと組み合わせて使用

リファレンスファイルを読み込んでから API を呼び出す流れ:

1. **Grep で必要なリファレンスを検索**:
```python
# 「経費精算」に関するリファレンスを探す
# Grep ツール: pattern="経費精算", path="skill/references"
```

2. **該当するリファレンスを読み込む**:
```python
# Read ツール: "skill/references/accounting-expense-applications.md"
# API の仕様、必須パラメータ、レスポンス形式を確認
```

3. **API を呼び出す**:
```python
# リファレンスの情報に基づいて API を呼び出す
session = FreeeSession()
result = session.post('/api/1/expense_applications', json_data={...})
```

## エラー対応

### 設定エラー

`[CONFIGURATION ERROR]` が表示される場合、エラーメッセージに示される設定ファイルパスを確認し、`client_id` と `client_secret` が正しく設定されているか確認する（`~/.config/freee-skill/config.json`）。

### 認証エラー

`AuthenticationError: Configuration is incomplete` または `401 Unauthorized` が発生した場合:

1. 設定ファイルが完全であることを確認
2. トークンの有効期限を確認
3. 認証情報が正しいことを確認

強制的に再認証するには:

```python
from skill.scripts.freee_session import FreeeSession

session = FreeeSession()
session.authenticate(force=True)
```

### トークンリフレッシュエラー

`TokenRefreshError` が発生した場合（リフレッシュトークンが無効）、トークンをクリアして再認証する:

```python
from skill.scripts.freee_session import FreeeSession

session = FreeeSession()
session.logout()
session.authenticate()
```

### API エラー

**権限エラー** (`403 Forbidden`):
1. freee 開発者ポータル（https://developer.freee.co.jp/）にアクセス
2. アプリケーション設定で権限スコープを確認
3. 必要な権限を追加して再認証

**リソースが見つからない** (`404` または `Company not found`):

利用可能なリソースを一覧表示して ID を確認する:

```python
from skill.scripts.freee_session import FreeeSession

session = FreeeSession()

# 利用可能な事業所を一覧表示
companies = session.get('/api/1/companies')
for company in companies['companies']:
    print(f"事業所: {company['display_name']} (ID: {company['id']})")
```

### エラーハンドリングのパターン

体系的にエラーを処理するには、以下のパターンを使用する:

```python
from skill.scripts.freee_session import (
    FreeeSession,
    AuthenticationError,
    APIError,
    TokenRefreshError
)

try:
    session = FreeeSession()
    session.authenticate()
    user = session.get('/api/1/users/me')
    print(user)

except AuthenticationError as e:
    print(f"認証エラー: {e}")
    # 設定ファイルを確認

except TokenRefreshError as e:
    print(f"トークンエラー: {e}")
    # 再認証が必要

except APIError as e:
    print(f"API エラー: {e}")
    print(f"ステータスコード: {e.status_code}")
    print(f"レスポンス: {e.response_data}")
```

詳細なトラブルシューティング手順は `references/troubleshooting.md` を参照する。
