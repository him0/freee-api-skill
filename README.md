# freee API スキル

> **注意**: このスキルは現在ベータ版です。

freee の API を MCP (Model Context Protocol) 経由で利用するための Claude スキルです。

## 概要

このスキルは、[@him0/freee-mcp](https://www.npmjs.com/package/@him0/freee-mcp) と組み合わせて使用することで、Claude Desktop から freee API を直接操作できるようにします。

**このスキルが提供するもの**:
- 62個の freee API リファレンスドキュメント（パラメータ、リクエストボディ、レスポンス情報を含む）
- freee-mcp の使い方ガイド
- API 呼び出しの具体例

**利用するには**:
1. ユーザー自身の環境で `npx @him0/freee-mcp configure` を実行（OAuth認証）
2. このスキルをプラグインとしてインストール（自動的に freee-mcp が MCP サーバーとして登録されます）
3. このスキルのリファレンスを参照しながら API を呼び出し

詳細は `skill/SKILL.md` を参照してください。

## 対応する freee API

このスキルでは、以下の freee API を利用できます：

- **会計 API** - 仕訳、勘定科目、取引先などの会計データの操作
- **人事労務 API** - 従業員情報、勤怠、給与などの人事労務データの操作
- **請求書 API** - 請求書の作成、更新、取得などの操作
- **工数管理 API** - プロジェクト、タスク、工数記録などの管理

## 開発

### リファレンスドキュメントの生成

OpenAPI スキーマからリファレンスドキュメントを生成するには、以下のコマンドを実行します：

```bash
bun run generate
```

このスクリプトは以下の処理を行います：

1. `openapi/` ディレクトリ内の OpenAPI スキーマファイルを読み込む
2. `openapi/tag-mappings.json` に基づいてタグごとにドキュメントを生成
3. `skill/references/` ディレクトリにマークダウンファイルを出力

生成されるドキュメントには、各エンドポイントの操作方法や説明が含まれます。
