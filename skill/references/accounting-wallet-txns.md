# Wallet txns

## 概要

口座明細

## エンドポイント一覧

### GET /api/1/wallet_txns

**操作**: 口座明細一覧の取得

**説明**: 概要 指定した事業所の口座明細一覧を取得する 定義 amount : 明細金額 due_amount : 取引登録待ち金額 balance : 残高 entry_side income : 入金 expense : 出金 walletable_type bank_account : 銀行口座 credit_card : クレジットカード wallet : その他の決済口座

### POST /api/1/wallet_txns

**操作**: 口座明細の作成

**説明**: 概要 指定した事業所の口座明細を作成する 定義 amount : 明細金額 due_amount : 取引登録待ち金額 balance : 残高 entry_side income : 入金 expense : 出金 walletable_type bank_account : 銀行口座 credit_card : クレジットカード wallet : その他の決済口座

### GET /api/1/wallet_txns/{id}

**操作**: 口座明細の取得

**説明**: 概要 指定した事業所の口座明細を取得する 定義 amount : 明細金額 due_amount : 取引登録待ち金額 balance : 残高 entry_side income : 入金 expense : 出金 walletable_type bank_account : 銀行口座 credit_card : クレジットカード wallet : その他の決済口座

### DELETE /api/1/wallet_txns/{id}

**操作**: 口座明細の削除

**説明**: 概要 指定した事業所の口座明細を削除する 注意点 同期をして取得したデータが「明細」の場合は、削除および再取得はできません。 詳細はfreeeヘルプセンターをご確認ください。



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [accounting-api-schema.json](../../openapi/accounting-api-schema.json)
