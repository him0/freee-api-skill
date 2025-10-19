# Partners

## 概要

取引先

## エンドポイント一覧

### GET /api/1/partners

**操作**: 取引先一覧の取得

**説明**: 概要 指定した事業所の取引先一覧を取得する 振込元口座ID（payer_walletable_id）, 振込手数料負担（transfer_fee_handling_side）は法人スタータープラン（および旧法人プロフェッショナルプラン）以上で利用可能です。

### POST /api/1/partners

**操作**: 取引先の作成

**説明**: 概要 指定した事業所の取引先を作成する 取引先名称（name）は重複不可です。 codeを利用するには、事業所の設定から取引先コードの利用を有効にする必要があります。 取引先コードの利用を有効にしている場合は、 codeの指定は必須です。 name、codeそれぞれ重複不可です。 振込元口座ID（payer_walletable_id）, 振込手数料負担（transfer_fee_handling_side）, 支払期日設定（payment_term_attributes）, 請求の入金期日設定（invoice_payment_term_attributes）は法人スタータープラン（および旧法人プロフェッショナルプラン）以上で利用可能です。

### GET /api/1/partners/{id}

**操作**: 取引先の取得

**説明**: 概要 指定した事業所の取引先を取得する 振込元口座ID（payer_walletable_id）, 振込手数料負担（transfer_fee_handling_side）, 支払期日設定（payment_term_attributes）, 請求の入金期日設定（invoice_payment_term_attributes）は法人スタータープラン（および旧法人プロフェッショナルプラン）以上で利用可能です。

### PUT /api/1/partners/{id}

**操作**: 取引先の更新

**説明**: 概要 指定した取引先の情報を更新する 取引先名称（name）は重複不可です。 codeを指定、更新することはできません。 振込元口座ID（payer_walletable_id）, 振込手数料負担（transfer_fee_handling_side）, 支払期日設定（payment_term_attributes）, 請求の入金期日設定（invoice_payment_term_attributes）は法人スタータープラン（および旧法人プロフェッショナルプラン）以上で利用可能です。 支払期日設定（payment_term_attributes）, 請求の入金期日設定（invoice_payment_term_attributes）にnull型を入力することにより、期日を未設定に変更可能です。

### DELETE /api/1/partners/{id}

**操作**: 取引先の削除

**説明**: 概要 指定した事業所の取引先を削除する

### PUT /api/1/partners/code/{code}

**操作**: 取引先コードでの取引先の更新

**説明**: 概要 取引先コードをキーに、指定した取引先の情報を更新する このAPIを利用するには、事業所の設定から取引先コードの利用を有効にする必要があります。 コードを日本語に設定している場合は、URLエンコードしてURLに含めるようにしてください。 取引先名称（name）は重複不可です。 振込元口座ID（payer_walletable_id）, 振込手数料負担（transfer_fee_handling_side）, 支払期日設定（payment_term_attributes）, 請求の入金期日設定（invoice_payment_term_attributes）は法人スタータープラン（および旧法人プロフェッショナルプラン）以上で利用可能です。 支払期日設定（payment_term_attributes）, 請求の入金期日設定（invoice_payment_term_attributes）にnull型を入力することにより、期日を未設定に変更可能です。

### PUT /api/1/partners/upsert_by_code

**操作**: 取引先の更新（存在しない場合は作成）

**説明**: 概要 取引先コードをキーに、指定した取引先の情報を更新（存在しない場合は作成）する このAPIを利用するには、事業所の設定から取引先コードの利用を有効にする必要があります。 取引先名称（name）は重複不可です。 振込元口座ID（payer_walletable_id）, 振込手数料負担（transfer_fee_handling_side）, 支払期日設定（payment_term_attributes）, 請求の入金期日設定（invoice_payment_term_attributes）は法人スタータープラン（および旧法人プロフェッショナルプラン）以上で利用可能です。 支払期日設定（payment_term_attributes）, 請求の入金期日設定（invoice_payment_term_attributes）にnull型を入力することにより、期日を未設定に変更可能です。



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [accounting-api-schema.json](../../openapi/accounting-api-schema.json)
