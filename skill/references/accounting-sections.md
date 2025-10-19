# Sections

## 概要

部門

## エンドポイント一覧

### GET /api/1/sections

**操作**: 部門一覧の取得

**説明**: 概要 指定した事業所の部門一覧を取得する 事業所の設定で部門コードを使用する設定にしている場合、レスポンスで部門コード(code)を返します レスポンスの例 GET https://api.freee.co.jp/api/1/sections?company_id=1 // プレミアムプラン、法人スタンダードプラン（および旧法人ベーシックプラン）以上 { &quot;sections&quot; : [ { &quot;id&quot; : 101, &quot;company_id&quot; : 1, &quot;name&quot; : &quot;開発部門&quot;, &quot;long_name&quot;: &quot;開発部門&quot;, &quot;shortcut1&quot; : &quot;DEVELOPER&quot;, &quot;shortcut2&quot; : &quot;123&quot;, &quot;indent_count&quot;: 1, &quot;parent_id&quot;: 11 }, ... ] } // それ以外のプラン ...

### POST /api/1/sections

**操作**: 部門の作成

**説明**: 概要 指定した事業所の部門を作成する codeを利用するには、事業所の設定で部門コードを使用する設定にする必要があります。 レスポンスの例 // プレミアムプラン、法人スタンダードプラン（および旧法人ベーシックプラン）以上 { &quot;section&quot; : { &quot;id&quot; : 102, &quot;company_id&quot; : 1, &quot;name&quot; : &quot;開発部門&quot;, &quot;shortcut1&quot; : &quot;DEVELOPER&quot;, &quot;shortcut2&quot; : &quot;123&quot;, &quot;indent_count&quot;: 1, &quot;parent_id&quot;: 101 } } // それ以外のプラン { &quot;section&quot; : { &quot;id&quot; : 102, &quot;company_id&quot; : 1, &quot;name&quot; : &quot;開発部門&quot;, &q...

### GET /api/1/sections/{id}

**操作**: 部門の取得

**説明**: 概要 指定した事業所の部門を取得する 事業所の設定で部門コードを使用する設定にしている場合、レスポンスで部門コード(code)を返します レスポンスの例 // プレミアムプラン、法人スタンダードプラン（および旧法人ベーシックプラン）以上 { &quot;section&quot; : { &quot;id&quot; : 102, &quot;company_id&quot; : 1, &quot;name&quot; : &quot;開発部門&quot;, &quot;long_name&quot;: &quot;開発部門&quot;, &quot;shortcut1&quot; : &quot;DEVELOPER&quot;, &quot;shortcut2&quot; : &quot;123&quot;, &quot;indent_count&quot;: 1, &quot;parent_id&quot;: 101 } } // それ以外のプラン { &quot;section&quot; : { &quot;id&quot; : 102, &quot;company_id&qu...

### PUT /api/1/sections/{id}

**操作**: 部門の更新

**説明**: 概要 指定した事業所の部門を更新する codeを利用するには、事業所の設定で部門コードを使用する設定にする必要があります。 レスポンスの例 // プレミアムプラン、法人スタンダードプラン（および旧法人ベーシックプラン）以上 { &quot;section&quot; : { &quot;id&quot; : 102, &quot;company_id&quot; : 1, &quot;name&quot; : &quot;開発部門&quot;, &quot;long_name&quot;: &quot;開発部門&quot;, &quot;shortcut1&quot; : &quot;DEVELOPER&quot;, &quot;shortcut2&quot; : &quot;123&quot;, &quot;indent_count&quot;: 1, &quot;parent_id&quot;: 101 } } // それ以外のプラン { &quot;section&quot; : { &quot;id&quot; : 102, &quot;company_id&quot; : 1...

### DELETE /api/1/sections/{id}

**操作**: 部門の削除

**説明**: 概要 指定した事業所の部門を削除する

### PUT /api/1/sections/code/upsert

**操作**: 部門の更新（存在しない場合は作成）

**説明**: 概要 部門コードをキーに、指定した部門の情報を更新（存在しない場合は作成）する 注意点 codeを利用するには、事業所の設定で部門コードを使用する設定にする必要があります。



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [accounting-api-schema.json](../../openapi/accounting-api-schema.json)
