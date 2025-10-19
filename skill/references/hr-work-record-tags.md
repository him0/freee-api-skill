# 勤怠タグ

## 概要

勤怠タグの操作

## エンドポイント一覧

### GET /api/v1/employees/{employee_id}/attendance_tags

**操作**: 勤怠タグ一覧の取得

**説明**: 概要 指定した従業員の利用可能な勤怠タグの一覧を返します。

### GET /api/v1/employees/{employee_id}/attendance_tags/{date}

**操作**: 勤怠タグと利用回数の取得

**説明**: 概要 指定した従業員・日付の勤怠タグと利用回数の一覧を返します。

### PUT /api/v1/employees/{employee_id}/attendance_tags/{date}

**操作**: 勤怠タグの更新

**説明**: 概要 指定した従業員・日付の勤怠タグを更新します。 注意点 指定した従業員・日付の勤怠タグが存在する場合は、上書き更新されます。 指定がなかった勤怠タグは削除されます。



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [hr-api-schema.json](../../openapi/hr-api-schema.json)
