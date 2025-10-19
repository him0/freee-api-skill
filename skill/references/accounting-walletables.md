# Walletables

## 概要

口座

## エンドポイント一覧

### GET /api/1/walletables

**操作**: 口座一覧の取得

**説明**: 概要 指定した事業所の口座一覧を取得する 定義 type bank_account : 銀行口座 credit_card : クレジットカード wallet : その他の決済口座 walletable_balance : 登録残高 last_balance : 同期残高 last_synced_at : 最終同期成功日時 sync_status : 同期ステータス

### POST /api/1/walletables

**操作**: 口座の作成

**説明**: 概要 指定した事業所の口座を作成する 注意点 同期に対応した口座はこのAPIでは作成できません 定義 type bank_account : 銀行口座 credit_card : クレジットカード wallet : その他の決済口座 name : 口座名 bank_id : 連携サービスID is_asset : type:wallet指定時に口座を資産口座とするか負債口座とするか（true: 資産口座 (デフォルト), false: 負債口座）

### GET /api/1/walletables/{type}/{id}

**操作**: 口座の取得

**説明**: 概要 指定した事業所の口座を取得する 定義 type bank_account : 銀行口座 credit_card : クレジットカード wallet : その他の決済口座 walletable_balance : 登録残高 last_balance : 同期残高 last_synced_at : 最終同期成功日時 sync_status : 同期ステータス

### PUT /api/1/walletables/{type}/{id}

**操作**: 口座の更新

**説明**: 概要 指定した事業所の口座を更新する

### DELETE /api/1/walletables/{type}/{id}

**操作**: 口座の削除

**説明**: 概要 指定した事業所の口座を削除する 注意点 削除を実行するには、当該口座に関連する仕訳データを事前に削除する必要があります。 当該口座に仕訳が残っていないか確認するには、レポートの「仕訳帳」等を参照し、必要に応じて、「取引」や「口座振替」も削除します。



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [accounting-api-schema.json](../../openapi/accounting-api-schema.json)
