# 従業員の基本給

## 概要

従業員の基本給の操作

## エンドポイント一覧

### GET /api/v1/employees/{employee_id}/basic_pay_rule

**操作**: 従業員の基本給の取得

**説明**: 概要 指定した従業員・日付の基本給情報を返します。 注意点 管理者権限を持ったユーザーのみ実行可能です。

### PUT /api/v1/employees/{employee_id}/basic_pay_rule

**操作**: 従業員の基本給の更新

**説明**: 概要 指定した従業員の基本給情報を更新します。 注意点 管理者権限を持ったユーザーのみ実行可能です。



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [hr-api-schema.json](../../openapi/hr-api-schema.json)
