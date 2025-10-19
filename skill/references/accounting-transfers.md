# Transfers

## 概要

取引（振替）

## エンドポイント一覧

### GET /api/1/transfers

**操作**: 取引（振替）一覧の取得

**説明**: 概要 指定した事業所の取引（振替）一覧を取得する 定義 amount : 振替金額 from_walletable_type, to_walletable_type bank_account : 銀行口座 credit_card : クレジットカード wallet : その他の決済口座

### POST /api/1/transfers

**操作**: 取引（振替）の作成

**説明**: 概要 指定した事業所の取引（振替）を作成する 定義 amount : 振替金額 from_walletable_type, to_walletable_type bank_account : 銀行口座 credit_card : クレジットカード wallet : その他の決済口座

### GET /api/1/transfers/{id}

**操作**: 取引（振替）の取得

**説明**: 概要 指定した事業所の取引（振替）を取得する 定義 amount : 振替金額 from_walletable_type, to_walletable_type bank_account : 銀行口座 credit_card : クレジットカード wallet : その他の決済口座

### PUT /api/1/transfers/{id}

**操作**: 取引（振替）の更新

**説明**: 概要 指定した事業所の取引（振替）を更新する 定義 amount : 振替金額 from_walletable_type, to_walletable_type bank_account : 銀行口座 credit_card : クレジットカード wallet : その他の決済口座

### DELETE /api/1/transfers/{id}

**操作**: 取引（振替）の削除

**説明**: 概要 指定した事業所の取引（振替）を削除する



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [accounting-api-schema.json](../../openapi/accounting-api-schema.json)
