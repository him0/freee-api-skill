# 年末調整

## 概要

年末調整の操作

## エンドポイント一覧

### GET /api/v1/yearend_adjustments/{year}/employees

**操作**: 年末調整対象一覧の取得

**説明**: 指定した年の年末調整対象のリスト返します。

### GET /api/v1/yearend_adjustments/{year}/employees/{employee_id}

**操作**: 年末調整の取得

**説明**: 指定した年、従業員IDの年末調整の詳細内容を返します。 年末調整対象外の従業員は、本人情報、給与・賞与、前職情報のみが取得できます。

### PUT /api/v1/yearend_adjustments/{year}/employees/{employee_id}

**操作**: 年末調整従業員情報の更新

**説明**: 概要 指定した従業員の姓名・住所などを更新します。 注意点 本APIは、年末調整が確定済みの従業員には非対応です。

### PUT /api/v1/yearend_adjustments/{year}/payroll_and_bonus/{employee_id}

**操作**: 年末調整従業員給与・賞与の更新

**説明**: 概要 指定した従業員の給与・賞与を更新します。 注意点 本APIは、年末調整が確定済みの従業員には非対応です。

### PUT /api/v1/yearend_adjustments/{year}/dependents/{employee_id}

**操作**: 年末調整家族情報の更新

**説明**: 概要 指定した年末調整の家族情報を更新します。 注意点 本APIは、年末調整が確定済みの従業員には非対応です。 idがない場合は新規作成、destroyがtrueの場合は削除になります。

### PUT /api/v1/yearend_adjustments/{year}/previous_jobs/{employee_id}

**操作**: 年末調整従業員前職情報の更新

**説明**: 概要 指定した従業員の前職情報を更新します。 注意点 本APIは、年末調整が確定済みの従業員には非対応です。

### DELETE /api/v1/yearend_adjustments/{year}/previous_jobs/{employee_id}

**操作**: 年末調整従業員前職情報の削除

**説明**: 概要 指定した従業員の前職情報を削除します。 注意点 本APIは、年末調整が確定済みの従業員には非対応です。

### POST /api/v1/yearend_adjustments/{year}/insurances/{employee_id}

**操作**: 年末調整従業員保険料情報の作成

**説明**: 概要 指定した従業員の保険料情報を作成します。 注意点 本APIは、年末調整が確定済みの従業員には非対応です。

### PUT /api/v1/yearend_adjustments/{year}/insurances/{employee_id}/{id}

**操作**: 年末調整従業員保険料情報の更新

**説明**: 概要 指定した従業員の保険料情報を更新します。 注意点 本APIは、年末調整が確定済みの従業員には非対応です。 certification_type="xml"の場合、recipient_first_name、recipient_last_name、recipient_relationshipのみが更新の対象となります。

### DELETE /api/v1/yearend_adjustments/{year}/insurances/{employee_id}/{id}

**操作**: 年末調整従業員保険料情報の削除

**説明**: 概要 指定した従業員の保険料情報を削除します。 注意点 本APIは、年末調整が確定済みの従業員には非対応です。

### PUT /api/v1/yearend_adjustments/{year}/housing_loan_deductions/{employee_id}

**操作**: 年末調整従業員住宅ローン控除額の更新

**説明**: 概要 指定した従業員の住宅ローン控除額を更新します。 注意点 本APIは、年末調整が確定済みの従業員には非対応です。

### POST /api/v1/yearend_adjustments/{year}/housing_loans/{employee_id}

**操作**: 年末調整従業員住宅ローンの作成

**説明**: 概要 指定した従業員の住宅ローンを作成します。 注意点 本APIは、年末調整が確定済みの従業員には非対応です。

### PUT /api/v1/yearend_adjustments/{year}/housing_loans/{employee_id}/{id}

**操作**: 年末調整従業員住宅ローンの更新

**説明**: 概要 指定した従業員の住宅ローンを更新します。 注意点 本APIは、年末調整が確定済みの従業員には非対応です。

### DELETE /api/v1/yearend_adjustments/{year}/housing_loans/{employee_id}/{id}

**操作**: 年末調整従業員住宅ローンの削除

**説明**: 概要 指定した従業員の住宅ローンを削除します。 注意点 本APIは、年末調整が確定済みの従業員には非対応です。



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [hr-api-schema.json](../../openapi/hr-api-schema.json)
