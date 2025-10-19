# 従業員のカスタム項目

## 概要

従業員のカスタム項目の操作

## エンドポイント一覧

### GET /api/v1/employees/{employee_id}/profile_custom_fields

**操作**: 従業員のカスタム項目の取得

**説明**: 概要 指定した従業員・日付のカスタム項目情報を返します。 注意点 管理者権限を持ったユーザーのみ実行可能です。 指定年月に在籍していない従業員および給与計算対象外の従業員ではデータが存在しないため、空の配列が返ります。



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [hr-api-schema.json](../../openapi/hr-api-schema.json)
