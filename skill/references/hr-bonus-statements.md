# 賞与明細

## 概要

賞与明細の操作

## エンドポイント一覧

### GET /api/v1/bonuses/employee_payroll_statements

**操作**: 賞与明細一覧の取得

**説明**: 概要 指定した事業所に所属する従業員の賞与明細をリストで返します。 指定した年月に支払いのある賞与明細が返されます。 注意点 管理者権限を持ったユーザーのみ実行可能です。

### GET /api/v1/bonuses/employee_payroll_statements/{employee_id}

**操作**: 賞与明細の取得

**説明**: 概要 指定した従業員ID、年月の賞与明細を返します。 指定した年月に支払いのある賞与明細が返されます。 注意点 管理者権限を持ったユーザーのみ実行可能です。 examples { "employee_payroll_statement": { "id": 1, "company_id": 1, "employee_id": 1, "employee_name": "給与 太郎", "employee_display_name": "給与 太郎", "employee_num": "001", "closing_date": "2018-03-31", "pay_date": "2018-03-31", "fixed": true, "calc_status": "calculated", "calculated_at": "2018-09-27T05:06:45.315Z", "bonus_amount": "300000.0", "total_allowance_amount": "0.0", "total_deduction_amount": "23830.0", "net_pay...



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [hr-api-schema.json](../../openapi/hr-api-schema.json)
