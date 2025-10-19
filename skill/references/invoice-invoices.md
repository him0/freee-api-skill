# Invoices

## 概要

請求書

## エンドポイント一覧

### GET /invoices

**操作**: 請求書一覧の取得


**説明**: 請求書の一覧を返します。

### POST /invoices

**操作**: 請求書の作成


**説明**: 請求書の作成をします。 issue_date, account_item_id, tax_code, item_id, section_id, tag_ids, segment_1_tag_id, segment_2_tag_id, segment_3_tag_id は、取引登録の下書き保存で利用されます。 tag_idsは10個まで設定可能です。

### GET /invoices/{id}

**操作**: 請求書の取得


**説明**: 指定されたIDの請求書を返します。

### PUT /invoices/{id}

**操作**: 請求書の更新


**説明**: 請求書の更新をします。 issue_date, account_item_id, tax_code, item_id, section_id, tag_ids, segment_1_tag_id, segment_2_tag_id, segment_3_tag_id は、取引登録の下書き保存で利用されます。 tag_idsは10個まで設定可能です。

### GET /invoices/templates

**操作**: 使用可能な請求書の帳票テンプレート一覧の取得


**説明**: 使用可能な請求書の帳票テンプレート一覧を返します。



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [invoice-api-schema.json](../../openapi/invoice-api-schema.json)
