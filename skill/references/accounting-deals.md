# Deals

## 概要

取引（収入・支出）

## エンドポイント一覧

### GET /api/1/deals

**操作**: 取引（収入・支出）一覧の取得

**説明**: 概要 指定した事業所の取引（収入・支出）一覧を取得する 定義 issue_date : 発生日 due_date : 支払期日 amount : 金額 due_amount : 支払残額 type income : 収入 expense : 支出 details : 取引の明細行 accruals : 取引の債権債務行 renews : 取引の+更新行 payments : 取引の支払行 from_walletable_type bank_account : 銀行口座 credit_card : クレジットカード wallet : 現金 private_account_item : プライベート資金（法人の場合は役員借入金もしくは役員借入金、個人の場合は事業主貸もしくは事業主借） 注意点 セグメントタグ情報は法人アドバンスプラン（および旧法人プロフェッショナルプラン）以上で利用可能です。利用可能なセグメントの数は、法人アドバンスプラン（および旧法人プロフェッショナルプラン）の場合は1つ、法人エンタープライズプランの場合は3つです。 partner_codeを利用するには、事業所の設定か...

### POST /api/1/deals

**操作**: 取引（収入・支出）の作成

**説明**: 概要 指定した事業所の取引（収入・支出）を作成する 定義 issue_date : 発生日 due_date : 支払期日 amount : 金額 due_amount : 支払残額 type income : 収入 expense : 支出 ref_number : 管理番号 details : 取引の明細行(最大40行) payments : 取引の支払行 receipt_ids : ファイルボックス（証憑ファイル）ID from_walletable_type bank_account : 銀行口座 credit_card : クレジットカード wallet : 現金 private_account_item : プライベート資金（法人の場合は役員借入金もしくは役員借入金、個人の場合は事業主貸もしくは事業主借） 注意点 本APIでは+更新行(renews)の操作ができません。取引（収入・支出）の+更新の作成APIをご利用ください。 セグメントタグ情報は法人アドバンスプラン（および旧法人プロフェッショナルプラン）以上で利用可能です。利用可能なセグメントの数は、法人アドバンスプラン（...

### GET /api/1/deals/{id}

**操作**: 取引（収入・支出）の取得

**説明**: 概要 指定した事業所の取引（収入・支出）を取得する 定義 issue_date : 発生日 due_date : 支払期日 amount : 金額 due_amount : 支払残額 type income : 収入 expense : 支出 details : 取引の明細行 accruals : 取引の債権債務行 renews : 取引の+更新行 payments : 取引の支払行 from_walletable_type bank_account : 銀行口座 credit_card : クレジットカード wallet : 現金 private_account_item : プライベート資金（法人の場合は役員借入金もしくは役員借入金、個人の場合は事業主貸もしくは事業主借） 注意点 セグメントタグ情報は法人アドバンスプラン（および旧法人プロフェッショナルプラン）以上で利用可能です。利用可能なセグメントの数は、法人アドバンスプラン（および旧法人プロフェッショナルプラン）の場合は1つ、法人エンタープライズプランの場合は3つです。

### PUT /api/1/deals/{id}

**操作**: 取引（収入・支出）の更新

**説明**: 概要 指定した事業所の取引（収入・支出）を更新する 定義 issue_date : 発生日 due_date : 支払期日 amount : 金額 due_amount : 支払残額 type income : 収入 expense : 支出 details : 取引の明細行(最大40行) renews : 取引の+更新行 payments : 取引の支払行 from_walletable_type bank_account : 銀行口座 credit_card : クレジットカード wallet : 現金 private_account_item : プライベート資金（法人の場合は役員借入金もしくは役員借入金、個人の場合は事業主貸もしくは事業主借） receipt_ids : ファイルボックス（証憑ファイル）ID 注意点 本APIでは支払行(payments)の操作ができません。取引（収入・支出）の支払行の作成・更新・削除APIをご利用ください。 本APIでは+更新行(renews)の操作ができません。取引（収入・支出）の+更新の作成・更新・削除APIをご利用ください。 本APIでは...

### DELETE /api/1/deals/{id}

**操作**: 取引（収入・支出）の削除

**説明**: 概要 指定した取引（収入・支出）を削除する



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [accounting-api-schema.json](../../openapi/accounting-api-schema.json)
