# 給与明細

## 概要

給与明細の操作

## エンドポイント一覧

### GET /api/v1/salaries/employee_payroll_statements

**操作**: 給与明細一覧の取得

**説明**: 概要 指定した事業所に所属する従業員の給与明細をリストで返します。 指定した年月に支払いのある給与明細が返されます。 注意点 複数時給を設定している場合はpaymentsに内訳が返されます。 管理者権限を持ったユーザーのみ実行可能です。 給与計算中の場合は、各パラメータはnullおよび空配列が返ります。

### GET /api/v1/salaries/employee_payroll_statements/{employee_id}

**操作**: 給与明細の取得

**説明**: 概要 指定した従業員ID、年月の給与明細を返します。 指定した年月に支払いのある給与明細が返されます。 注意点 複数時給を設定している場合はpaymentsに内訳が返されます。 管理者権限を持ったユーザーのみ実行可能です。 給与計算中の場合は、各パラメータはnullおよび空配列が返ります。 examples { "employee_payroll_statement": { "id": 1, "company_id": 1, "employee_id": 1, "employee_name": "給与 太郎", "employee_display_name": "給与 太郎", "employee_num": "001", "pay_date": "2018-02-25", "start_date": "2018-02-01", "closing_date": "2018-02-28", "variable_pay_start_date": "2018-01-01", "variable_pay_closing_date": "2018-01-31", "fixed": true, "...



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [hr-api-schema.json](../../openapi/hr-api-schema.json)
