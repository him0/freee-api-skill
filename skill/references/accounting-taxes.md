# Taxes

## 概要

税区分

## エンドポイント一覧

### GET /api/1/taxes/codes

**操作**: 税区分一覧の取得（廃止予定）

**説明**: 概要 税区分一覧を取得する 注意点 このAPIは廃止予定のため非推奨です。api/1/taxes/companies/{company_id}（指定した事業所の税区分一覧の取得）をご利用ください。

### GET /api/1/taxes/codes/{code}

**操作**: 税区分の取得

**説明**: 概要 税区分を取得する

### GET /api/1/taxes/companies/{company_id}

**操作**: 指定した事業所の税区分一覧の取得

**説明**: 概要 指定した事業所の税区分一覧を取得する



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [accounting-api-schema.json](../../openapi/accounting-api-schema.json)
