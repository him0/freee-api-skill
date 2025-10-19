# DeliverySlips

## 概要

納品書

## エンドポイント一覧

### GET /delivery_slips

**操作**: 納品書一覧の取得


**説明**: 納品書の一覧を返します。

### POST /delivery_slips

**操作**: 納品書の作成


**説明**: 納品書の作成をします。 issue_date, account_item_id, tax_code, item_id, section_id, tag_ids, segment_1_tag_id, segment_2_tag_id, segment_3_tag_id は、取引登録の下書き保存で利用されます。 tag_idsは10個まで設定可能です。

### GET /delivery_slips/{id}

**操作**: 納品書の取得


**説明**: 指定されたIDの納品書を返します。

### PUT /delivery_slips/{id}

**操作**: 納品書の更新


**説明**: 納品書の更新をします。 issue_date, account_item_id, tax_code, item_id, section_id, tag_ids, segment_1_tag_id, segment_2_tag_id, segment_3_tag_id は、取引登録の下書き保存で利用されます。 tag_idsは10個まで設定可能です。

### GET /delivery_slips/templates

**操作**: 使用可能な納品書の帳票テンプレート一覧の取得


**説明**: 使用可能な納品書の帳票テンプレート一覧を返します。



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [invoice-api-schema.json](../../openapi/invoice-api-schema.json)
