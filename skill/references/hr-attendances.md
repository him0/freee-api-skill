# 勤怠

## 概要

勤怠の操作

## エンドポイント一覧

### GET /api/v1/employees/{employee_id}/work_records/{date}

**操作**: 勤怠の取得

**説明**: 概要 指定した従業員・日付の勤怠情報を返します。

### PUT /api/v1/employees/{employee_id}/work_records/{date}

**操作**: 勤怠の更新

**説明**: 概要 指定した従業員の勤怠情報を更新します。 注意点 振替出勤・振替休日・代休出勤・代休の登録はAPIでは行うことができません。 examples 出勤日について出退勤時刻および休憩時間を更新する場合は以下のようなパラメータをリクエストします。 { "company_id": 1, "break_records": [ { "clock_in_at": "2017-05-25 12:00:00", "clock_out_at": "2017-05-25 13:00:00" } ], "work_record_segments": [ { "clock_in_at": "2017-05-25 09:10:00", "clock_out_at": "2017-05-25 18:20:00" } ] } 勤務パターンや既定の所定労働時間を変更する場合は use_default_work_pattern に false を指定するとともに、各設定を上書きするパラメータをリクエストします。 { "company_id": 1, "break_records": [ { "clock_in_at"...

### DELETE /api/v1/employees/{employee_id}/work_records/{date}

**操作**: 勤怠の削除

**説明**: 概要 指定した従業員の勤怠情報を削除します。



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [hr-api-schema.json](../../openapi/hr-api-schema.json)
