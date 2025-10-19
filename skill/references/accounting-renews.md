# Renews

## 概要

取引（収入・支出）の+更新

## エンドポイント一覧

### POST /api/1/deals/{id}/renews

**操作**: 取引（収入・支出）の+更新の作成

**説明**: 概要 指定した事業所の取引（収入・支出）の+更新を作成する 定義 issue_date : 発生日 due_date : 支払期日 amount : 金額 due_amount : 支払残額 type income : 収入 expense : 支出 details : 取引の明細行 accruals : 取引の債権債務行 renews : 取引の+更新行 payments : 取引の支払行 from_walletable_type bank_account : 銀行口座 credit_card : クレジットカード wallet : 現金 private_account_item : プライベート資金（法人の場合は役員借入金もしくは役員借入金、個人の場合は事業主貸もしくは事業主借） 注意点 本APIではdetails(取引の明細行)、accruals(債権債務行)、renewsのdetails(+更新の明細行)のみ操作可能です。 本APIで取引を更新すると、消費税の計算方法は必ず内税方式が選択されます。

### PUT /api/1/deals/{id}/renews/{renew_id}

**操作**: 取引（収入・支出）の+更新の更新

**説明**: 概要 指定した事業所の取引（収入・支出）の+更新を更新する 定義 issue_date : 発生日 due_date : 支払期日 amount : 金額 due_amount : 支払残額 type income : 収入 expense : 支出 details : 取引の明細行 accruals : 取引の債権債務行 renews : 取引の+更新行 payments : 取引の支払行 from_walletable_type bank_account : 銀行口座 credit_card : クレジットカード wallet : 現金 private_account_item : プライベート資金（法人の場合は役員借入金もしくは役員借入金、個人の場合は事業主貸もしくは事業主借） 注意点 本APIでは+更新の更新のみ可能です。取引や支払行に対する更新はできません。 renew_idにはrenewsのid(+更新ID)を指定してください。renewsのdetailsのid(+更新の明細行ID)を指定できません。 月締めされている仕訳に紐づく＋更新行の編集・削除はできません。 承認済み...

### DELETE /api/1/deals/{id}/renews/{renew_id}

**操作**: 取引（収入・支出）の+更新の削除

**説明**: 概要 指定した事業所の取引（収入・支出）の+更新を削除する 注意点 本APIでは+更新の削除のみ可能です。取引や支払行に対する削除はできません。 renew_idにはrenewsのid(+更新ID)を指定してください。renewsのdetailsのid(+更新の明細行ID)を指定できません。 月締めされている仕訳に紐づく＋更新行の編集・削除はできません。 承認済み仕訳に紐づく＋更新行の編集・削除は管理者権限のユーザーのみ可能です。 本APIで取引を更新すると、消費税の計算方法は必ず内税方式が選択されます。



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [accounting-api-schema.json](../../openapi/accounting-api-schema.json)
