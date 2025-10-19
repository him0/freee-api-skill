# 従業員の家族情報

## 概要

従業員の家族情報の操作

## エンドポイント一覧

### GET /api/v1/employees/{employee_id}/dependent_rules

**操作**: 従業員の家族情報の取得

**説明**: 概要 指定した従業員・日付の家族情報を返します。

### PUT /api/v1/employees/{employee_id}/dependent_rules/bulk_update

**操作**: 従業員の家族情報の更新

**説明**: 概要 指定した従業員の家族情報を更新します。 注意点 idがない場合は新規作成、destroyがtrueの場合は削除になります。 residence_type=live_in: 同居の場合、以下のパラメータに指定した値はWebに反映されません。 zipcode1 zipcode2 prefecture_code address address_kana annual_remittance_amount residence_type=non_resident: 別居(国外)の場合、以下のパラメータに指定した値はWebに反映されません。 prefecture_code



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [hr-api-schema.json](../../openapi/hr-api-schema.json)
