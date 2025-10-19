# Fixed assets

## 概要

固定資産台帳

## エンドポイント一覧

### GET /api/1/fixed_assets

**操作**: 固定資産一覧の取得

**説明**: 概要 指定した事業所の固定資産一覧を取得する 定義 このAPIは法人エンタープライズに加入している事業所のみが利用できます。 target_date : 表示したい会計期間の開始年月日。開始年月日以外を指定した場合は、その日付が含まれる会計期間が対象となります。 depreciation_amount : 本年分の償却費合計 depreciation_method : 償却方法 depreciation_account_item_id : 減価償却に使う勘定科目 acquisition_cost : 取得価額 opening_balance : 期首残高 undepreciated_balance : 未償却残高。土地などの償却しない固定資産はnullが返ります。 opening_accumulated_depreciation : 期首減価償却累計額 closing_accumulated_depreciation : 期末減価償却累計額 注意点 up_to_dateがfalseの場合、残高の集計が完了していません。最新の集計結果を確認したい場合は、時間を空けて再度取得する必要があり...



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [accounting-api-schema.json](../../openapi/accounting-api-schema.json)
