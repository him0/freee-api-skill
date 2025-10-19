# 勤怠タグサマリ

## 概要

勤怠タグサマリの操作

## エンドポイント一覧

### GET /api/v1/employees/{employee_id}/attendance_tag_summaries/{year}/{month}

**操作**: 勤怠タグ月次サマリの取得

**説明**: 概要 指定した従業員・年月の勤怠タグサマリを更新します。 年月は給与支払い月を指定してください。

### PUT /api/v1/employees/{employee_id}/attendance_tag_summaries/{year}/{month}

**操作**: 勤怠タグ月次サマリの更新

**説明**: 概要 指定した従業員・年月の勤怠タグサマリを更新します。 年月は給与支払い月を指定してください。 注意点 管理者権限を持ったユーザーのみ実行可能です。 指定した従業員・年月の勤怠タグサマリが存在する場合は、上書き更新されます。 指定がなかった勤怠タグは自動的に0が設定されます。



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [hr-api-schema.json](../../openapi/hr-api-schema.json)
