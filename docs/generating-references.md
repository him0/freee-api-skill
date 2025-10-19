# OpenAPIスキーマからリファレンスドキュメントを生成する手順

このドキュメントでは、OpenAPIスキーマファイルから機能別のリファレンスドキュメントを自動生成する方法を説明します。

## 概要

OpenAPI仕様のJSONファイルから、各機能（タグ）ごとにMarkdown形式のリファレンスドキュメントを生成します。`scripts/generate_references.sh` スクリプトを使用して、すべてのリファレンスドキュメントを一括生成できます。

ファイル名は `openapi/tag-mappings.json` で定義された英語名を使用します。これにより、2バイト文字を含むファイル名の問題を回避し、可読性の高いファイル名を維持します。

## 前提条件

### 必要なツール

- `jq` - JSONプロセッサ（インストール: `brew install jq`）
- `bash` - シェルスクリプト実行環境

### 必要なファイル

- OpenAPI 3.0形式のスキーマファイル（JSON）: `openapi/*-api-schema.json`
- タグマッピングファイル: `openapi/tag-mappings.json`

## ディレクトリ構成

```
project-root/
├── openapi/
│   ├── tag-mappings.json           # タグ名と英語ファイル名のマッピング
│   ├── accounting-api-schema.json  # 会計APIスキーマ
│   ├── hr-api-schema.json          # 人事労務APIスキーマ
│   ├── invoice-api-schema.json     # 請求書APIスキーマ
│   └── pm-api-schema.json          # プロジェクト管理APIスキーマ
├── scripts/
│   └── generate_references.sh      # リファレンス生成スクリプト
├── skill/
│   └── references/                 # 生成されるリファレンスドキュメント
└── docs/
    └── generating-references.md    # このドキュメント
```

## 生成手順

### クイックスタート

すべてのリファレンスドキュメントを一括生成するには、以下のコマンドを実行します：

```bash
# プロジェクトルートから実行
bash scripts/generate_references.sh
```

このスクリプトは以下を自動で行います：

1. `openapi/tag-mappings.json` からタグマッピングを読み込み
2. 各APIスキーマファイルからタグとエンドポイント情報を抽出
3. 英語ファイル名で `skill/references/` にMarkdownファイルを生成

### 実行例

```bash
$ bash scripts/generate_references.sh

Starting reference document generation...
========================================

Processing accounting-api...
================================
Generated: accounting-partners.md
Generated: accounting-selectables.md
Generated: accounting-account-items.md
...
Generated 31 files for accounting-api

Processing hr-api...
================================
Generated: hr-login-user.md
Generated: hr-employees.md
...
Generated 27 files for hr-api

Processing invoice-api...
================================
Generated: invoice-invoices.md
Generated: invoice-quotations.md
Generated: invoice-delivery-slips.md
Generated 3 files for invoice-api

Processing pm-api...
================================
Generated: pm-users.md
Generated 1 files for pm-api

========================================
Reference generation complete!
Output directory: /Users/him0/src/freee-api-skill/skill/references
```

## 生成されるドキュメントの形式

各Markdownファイルは以下の構成になります：

```markdown
# [機能名]

## 概要

[機能の説明]

## エンドポイント一覧

### GET /api/1/xxx
**操作**: [操作の概要]
**説明**: [詳細な説明]

### POST /api/1/xxx
**操作**: [操作の概要]
**説明**: [詳細な説明]

## 参考情報

- API公式ドキュメント: [URL]
- OpenAPIスキーマ: [相対パス]
```

## タグマッピングファイル

`openapi/tag-mappings.json` は、各APIのタグ名と英語ファイル名のマッピングを定義します。

### 構造

```json
{
  "accounting-api": {
    "Partners": "partners",
    "Deals": "deals",
    "従業員": "employees"
  },
  "hr-api": {
    "ログインユーザー": "login-user",
    "従業員": "employees"
  }
}
```

### 新しいタグを追加する

新しいタグが追加された場合は、マッピングファイルを更新してから生成スクリプトを実行します：

```bash
# 1. OpenAPIスキーマから新しいタグを確認
jq '.tags[] | {name: .name, description: .description}' \
  openapi/accounting-api-schema.json

# 2. openapi/tag-mappings.json に新しいマッピングを追加
# 例: "NewTag": "new-tag"

# 3. リファレンスを再生成
bash scripts/generate_references.sh
```

## カスタマイズ方法

### 1. ファイル名を変更

`openapi/tag-mappings.json` を編集して英語ファイル名を変更します：

```json
{
  "accounting-api": {
    "Partners": "business-partners"  // "partners" から変更
  }
}
```

### 2. 説明文の長さ制限を調整

`scripts/generate_references.sh` の以下の行を編集：

```bash
if [ ${#description} -gt 500 ]; then
    description="${description:0:500}..."
fi
```

数値 `500` を変更することで最大文字数を調整できます。

### 3. ドキュメントテンプレートの変更

`scripts/generate_references.sh` 内の `MARKDOWN` ヒアドキュメント部分を編集してテンプレートをカスタマイズできます。

## 検証とトラブルシューティング

### 生成結果の確認

```bash
# 生成されたファイル数を確認
ls -1 skill/references/*.md | wc -l

# ファイル一覧を表示
ls -1 skill/references/

# サンプルファイルをチェック
head -30 skill/references/accounting-partners.md
```

### よくある問題

#### 問題1: jqコマンドが見つからない

```bash
# macOSの場合
brew install jq

# Ubuntuの場合
sudo apt-get install jq
```

#### 問題2: マッピングファイルが見つからない

エラー: `Error: Tag mappings file not found`

```bash
# マッピングファイルの存在を確認
ls -la openapi/tag-mappings.json

# プロジェクトルートで実行していることを確認
pwd  # /path/to/freee-api-skill であるべき
```

#### 問題3: 新しいタグが生成されない

1. OpenAPIスキーマに新しいタグが存在することを確認
2. `openapi/tag-mappings.json` に対応するマッピングが存在することを確認
3. スクリプトを再実行

```bash
# タグの存在確認
jq '.tags[] | .name' openapi/accounting-api-schema.json

# マッピングの確認
jq '.["accounting-api"]' openapi/tag-mappings.json
```

#### 問題4: ファイル名に2バイト文字が含まれる

すべてのファイル名が英語になっていることを確認：

```bash
# 2バイト文字を含むファイルを検索
find skill/references -name '*[^[:ascii:]]*'

# 見つかった場合は、tag-mappings.json を確認
```

## 応用例

### 特定のAPIのみ生成

スクリプトを編集して特定のAPIのみ処理するようコメントアウト：

```bash
# scripts/generate_references.sh の末尾で以下をコメントアウト
process_api "accounting-api" "$OPENAPI_DIR/accounting-api-schema.json" "accounting"
# process_api "hr-api" "$OPENAPI_DIR/hr-api-schema.json" "hr"  # コメントアウト
# process_api "invoice-api" "$OPENAPI_DIR/invoice-api-schema.json" "invoice"  # コメントアウト
# process_api "pm-api" "$OPENAPI_DIR/pm-api-schema.json" "pm"  # コメントアウト
```

### 生成ログの保存

```bash
bash scripts/generate_references.sh 2>&1 | tee generation.log
```

### CI/CDでの自動生成

OpenAPIスキーマが更新された際に自動的にリファレンスを再生成：

```yaml
# .github/workflows/generate-docs.yml
name: Generate API References

on:
  push:
    paths:
      - 'openapi/*.json'

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install jq
        run: sudo apt-get install -y jq
      - name: Generate references
        run: bash scripts/generate_references.sh
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add skill/references/
          git commit -m "Update API references" || echo "No changes"
          git push
```

## まとめ

この手順により：

1. ✅ 英語ファイル名で2バイト文字問題を解決
2. ✅ タグマッピングファイルで柔軟なファイル名管理
3. ✅ 1つのコマンドで全リファレンスを自動生成
4. ✅ 統一されたフォーマットで保守性が高い
5. ✅ 新しいタグの追加が容易

生成されたドキュメントは、必要に応じて手動で詳細を追加することも可能です。
