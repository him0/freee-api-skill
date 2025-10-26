---
name: freee-api-skill
description: "freee 会計・人事労務 API を MCP 経由で操作するスキル。62個の詳細なAPIリファレンスと使い方ガイドを提供。"
---

# freee API スキル

## 概要

[@him0/freee-mcp](https://www.npmjs.com/package/@him0/freee-mcp) (MCP サーバー) を通じて freee API と連携。

**このスキルの役割**:
- freee API の詳細リファレンス（62ファイル）を提供
- freee-mcp 使用ガイドとAPI呼び出し例を提供

**注意**: OAuth認証はユーザー自身が自分の環境で実行する必要があります。

## セットアップ

### 1. OAuth 認証（あなたのターミナルで実行）

```bash
npx @him0/freee-mcp configure
```

ブラウザでfreeeにログインし、事業所を選択します。設定は `~/.config/freee-mcp/config.json` に保存されます。

### 2. プラグインをインストール

- **Claude Code**: コマンドパレット → "Claude: Install Plugin" → このリポジトリのパス
- **Claude Desktop**: 設定 → Plugins → Add Plugin → このリポジトリのパス

### 3. 再起動して確認

Claude を再起動後、`freee_help` ツールが利用可能か確認。

## リファレンス

62個のAPIリファレンスが `references/` に含まれます。各リファレンスにはパラメータ、リクエストボディ、レスポンスの詳細情報があります。

**検索方法**:
```
pattern: "経費"
path: "skill/references"
output_mode: "files_with_matches"
```

**主なリファレンス**:
- `accounting-deals.md` - 取引
- `accounting-expense-applications.md` - 経費申請
- `hr-employees.md` - 従業員情報
- `hr-attendances.md` - 勤怠

## 使い方

### MCPツール

**認証・事業所管理**:
- `freee_authenticate` - OAuth認証
- `freee_auth_status` - 認証状態確認
- `freee_list_companies` - 事業所一覧
- `freee_set_company` - 事業所切り替え

**API呼び出し**:
- `freee_api_get` - GETリクエスト
- `freee_api_post` - POSTリクエスト
- `freee_api_put` - PUTリクエスト
- `freee_api_delete` - DELETEリクエスト
- `freee_api_patch` - PATCHリクエスト

### 基本ワークフロー

1. **リファレンスを検索**: Grepで `skill/references` を検索
2. **仕様を確認**: 該当するリファレンスを読む
3. **APIを呼び出す**: `freee_api_*` ツールを使用

### 使用例

**経費申請を作成**:
```
# 1. リファレンスを確認
Read: "skill/references/accounting-expense-applications.md"

# 2. APIを呼び出す
freee_api_post {
  "path": "/api/1/expense_applications",
  "body": {
    "company_id": 123456,
    "title": "交通費",
    "issue_date": "2025-01-15",
    "expense_application_lines": [{
      "transaction_date": "2025-01-15",
      "description": "新宿→渋谷",
      "amount": 400
    }]
  }
}
```

**取引を検索**:
```
freee_api_get {
  "path": "/api/1/deals",
  "query": {
    "company_id": 123456,
    "limit": 10
  }
}
```

**従業員情報を取得**（人事労務API）:
```
freee_api_get {
  "path": "/hr/api/v1/employees",
  "query": {
    "company_id": 123456,
    "year": 2025,
    "month": 1
  }
}
```

## エラー対応

- **認証エラー**: `freee_auth_status` で確認 → `freee_clear_auth` → `freee_authenticate`
- **事業所エラー**: `freee_list_companies` → `freee_set_company`
- **詳細**: `references/troubleshooting.md` 参照

## 対応API

- **会計**: `/api/1/...`
- **人事労務**: `/hr/api/v1/...`
- **請求書**: `/iv/api/v1/...`
- **工数管理**: `/pm/api/v1/...`

パスから自動的に正しいエンドポイントが選択されます。

## 関連リンク

- [freee-mcp](https://www.npmjs.com/package/@him0/freee-mcp)
- [freee API ドキュメント](https://developer.freee.co.jp/docs)
