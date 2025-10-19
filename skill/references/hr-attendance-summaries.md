# 勤怠情報サマリ

## 概要

勤怠情報の月次サマリの操作

## エンドポイント一覧

### GET /api/v1/employees/{employee_id}/work_record_summaries/{year}/{month}

**操作**: 勤怠情報月次サマリの取得

**説明**: 概要 指定した従業員、月の勤怠情報のサマリを返します。 注意点 work_recordsオプションにtrueを指定することで、明細となる日次の勤怠情報もあわせて返却します。

### PUT /api/v1/employees/{employee_id}/work_record_summaries/{year}/{month}

**操作**: 勤怠情報月次サマリの更新

**説明**: 概要 指定した従業員、月の勤怠情報のサマリを更新します。 注意点 管理者権限を持ったユーザーのみ実行可能です。 日毎の勤怠の更新はこのAPIではできません。日毎の勤怠の操作には勤怠APIを使用して下さい。 勤怠データが存在しない場合は新規作成、既に存在する場合は上書き更新されます。 値が設定された項目のみ更新されます。値が設定されなかった場合は自動的に0が設定されます。



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [hr-api-schema.json](../../openapi/hr-api-schema.json)
