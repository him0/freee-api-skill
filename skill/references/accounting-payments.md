# Payments

## 概要

取引（収入・支出）の支払行

## エンドポイント一覧

### POST /api/1/deals/{id}/payments

**操作**: 取引（収入・支出）の支払行の作成

**説明**: 概要 指定した事業所の取引（収入・支出）の支払行を作成する 定義 issue_date : 発生日 due_date : 支払期日 amount : 金額 due_amount : 支払残額 type income : 収入 expense : 支出 details : 取引の明細行 renews : 取引の+更新行 payments : 取引の支払行 from_walletable_type bank_account : 銀行口座 credit_card : クレジットカード wallet : 現金 private_account_item : プライベート資金（法人の場合は役員借入金もしくは役員借入金、個人の場合は事業主貸もしくは事業主借）

### PUT /api/1/deals/{id}/payments/{payment_id}

**操作**: 取引（収入・支出）の支払行の更新

**説明**: 概要 指定した事業所の取引（収入・支出）の支払行を更新する 定義 issue_date : 発生日 due_date : 支払期日 amount : 金額 due_amount : 支払残額 type income : 収入 expense : 支出 details : 取引の明細行 renews : 取引の+更新行 payments : 取引の支払行 from_walletable_type bank_account : 銀行口座 credit_card : クレジットカード wallet : 現金 private_account_item : プライベート資金（法人の場合は役員借入金もしくは役員借入金、個人の場合は事業主貸もしくは事業主借）

### DELETE /api/1/deals/{id}/payments/{payment_id}

**操作**: 取引（収入・支出）の支払行の削除

**説明**: 概要 指定した事業所の取引（収入・支出）の支払行を削除する 定義 issue_date : 発生日 due_date : 支払期日 amount : 金額 due_amount : 支払残額 type income : 収入 expense : 支出 details : 取引の明細行



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [accounting-api-schema.json](../../openapi/accounting-api-schema.json)
