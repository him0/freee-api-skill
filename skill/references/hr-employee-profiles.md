# 従業員の姓名・住所など

## 概要

従業員の姓名・住所などの操作

## エンドポイント一覧

### GET /api/v1/employees/{employee_id}/profile_rule

**操作**: 従業員の姓名・住所などの取得

**説明**: 概要 指定した従業員・日付の姓名などの情報を返します。 注意点 本APIは、給与計算対象外の従業員には非対応です。employee_idに給与計算対象外の従業員IDを指定した場合、本APIを利用できません。

### PUT /api/v1/employees/{employee_id}/profile_rule

**操作**: 従業員の姓名・住所などの更新

**説明**: 概要 指定した従業員の姓名・住所などを更新します。 注意点 本APIは、給与計算対象外の従業員には非対応です。employee_idに給与計算対象外の従業員IDを指定した場合、本APIを利用できません。



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [hr-api-schema.json](../../openapi/hr-api-schema.json)
