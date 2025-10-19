# Trial balance

## 概要

試算表

## エンドポイント一覧

### GET /api/1/reports/trial_bs

**操作**: 貸借対照表の取得

**説明**: 概要 指定した事業所の貸借対照表を取得する 定義 created_at : 作成日時 account_item_name : 勘定科目名 hierarchy_level: 階層レベル parent_account_category_name: 上位勘定科目カテゴリー名 opening_balance : 期首残高 debit_amount : 借方金額 credit_amount: 貸方金額 closing_balance : 期末残高 composition_ratio : 構成比 注意点 会計年度が指定されない場合、現在の会計年度がデフォルトとなります。 up_to_dateがfalseの場合、残高の集計が完了していません。最新の集計結果を確認したい場合は、時間を空けて再度取得する必要があります。 partner_codeとpartner_idは同時に指定することはできません。 start_date / end_date を指定した場合、以下を同時に指定することはできません。 fiscal_year start_month end_month 0を指定すると未選択で絞り込めます p...

### GET /api/1/reports/trial_bs_two_years

**操作**: 貸借対照表(前年比較)の取得

**説明**: 概要 指定した事業所の貸借対照表(前年比較)を取得する 定義 created_at : 作成日時 account_item_name : 勘定科目名 hierarchy_level: 階層レベル parent_account_category_name: 上位勘定科目カテゴリー名 last_year_closing_balance: 前年度期末残高 closing_balance : 期末残高 year_on_year : 前年比 注意点 会計年度が指定されない場合、現在の会計年度がデフォルトとなります。 up_to_dateがfalseの場合、残高の集計が完了していません。最新の集計結果を確認したい場合は、時間を空けて再度取得する必要があります。 partner_codeとpartner_idは同時に指定することはできません。 start_date / end_date を指定した場合、以下を同時に指定することはできません。 fiscal_year start_month end_month 0を指定すると未選択で絞り込めます partner_idに0を指定して絞り込んだ場合 取引先...

### GET /api/1/reports/trial_bs_three_years

**操作**: 貸借対照表(３期間比較)の取得

**説明**: 概要 指定した事業所の貸借対照表(３期間比較)を取得する 定義 created_at : 作成日時 account_item_name : 勘定科目名 hierarchy_level: 階層レベル parent_account_category_name: 上位勘定科目カテゴリー名 two_years_before_closing_balance: 前々年度期末残高 last_year_closing_balance: 前年度期末残高 closing_balance : 期末残高 year_on_year : 前年比 注意点 会計年度が指定されない場合、現在の会計年度がデフォルトとなります。 up_to_dateがfalseの場合、残高の集計が完了していません。最新の集計結果を確認したい場合は、時間を空けて再度取得する必要があります。 partner_codeとpartner_idは同時に指定することはできません。 start_date / end_date を指定した場合、以下を同時に指定することはできません。 fiscal_year start_month end_month 0を...

### GET /api/1/reports/trial_pl

**操作**: 損益計算書の取得

**説明**: 概要 指定した事業所の損益計算書を取得する 定義 created_at : 作成日時 account_item_name : 勘定科目名 hierarchy_level: 階層レベル parent_account_category_name: 上位勘定科目カテゴリー名 opening_balance : 期首残高 debit_amount : 借方金額 credit_amount: 貸方金額 closing_balance : 期末残高 composition_ratio : 構成比 注意点 会計年度が指定されない場合、現在の会計年度がデフォルトとなります。 up_to_dateがfalseの場合、残高の集計が完了していません。最新の集計結果を確認したい場合は、時間を空けて再度取得する必要があります。 配賦仕訳の絞り込み（cost_allocation）は法人スタンダードプラン（および旧法人ベーシックプラン）以上で利用可能です。 partner_codeとpartner_idは同時に指定することはできません。 start_date / end_date を指定した場合、以下を同時に指定...

### GET /api/1/reports/trial_pl_two_years

**操作**: 損益計算書(前年比較)の取得

**説明**: 概要 指定した事業所の損益計算書(前年比較)を取得する 定義 created_at : 作成日時 account_item_name : 勘定科目名 hierarchy_level: 階層レベル parent_account_category_name: 上位勘定科目カテゴリー名 last_year_closing_balance: 前年度期末残高 closing_balance : 期末残高 year_on_year : 前年比 注意点 会計年度が指定されない場合、現在の会計年度がデフォルトとなります。 up_to_dateがfalseの場合、残高の集計が完了していません。最新の集計結果を確認したい場合は、時間を空けて再度取得する必要があります。 配賦仕訳の絞り込み（cost_allocation）は法人スタンダードプラン（および旧法人ベーシックプラン）以上で利用可能です。 partner_codeとpartner_idは同時に指定することはできません。 start_date / end_date を指定した場合、以下を同時に指定することはできません。 fiscal_year sta...

### GET /api/1/reports/trial_pl_three_years

**操作**: 損益計算書(３期間比較)の取得

**説明**: 概要 指定した事業所の損益計算書(３期間比較)を取得する 定義 created_at : 作成日時 account_item_name : 勘定科目名 hierarchy_level: 階層レベル parent_account_category_name: 上位勘定科目カテゴリー名 two_years_before_closing_balance: 前々年度期末残高 last_year_closing_balance: 前年度期末残高 closing_balance : 期末残高 year_on_year : 前年比 注意点 会計年度が指定されない場合、現在の会計年度がデフォルトとなります。 up_to_dateがfalseの場合、残高の集計が完了していません。最新の集計結果を確認したい場合は、時間を空けて再度取得する必要があります。 配賦仕訳の絞り込み（cost_allocation）は法人スタンダードプラン（および旧法人ベーシックプラン）以上で利用可能です。 partner_codeとpartner_idは同時に指定することはできません。 start_date / end_date...

### GET /api/1/reports/trial_pl_sections

**操作**: 損益計算書(部門比較)の取得

**説明**: 概要 指定した事業所の損益計算書(部門比較)を取得する 定義 created_at : 作成日時 account_item_name : 勘定科目名 hierarchy_level: 階層レベル parent_account_category_name: 上位勘定科目カテゴリー名 closing_balance : 期末残高 注意点 会計年度が指定されない場合、現在の会計年度がデフォルトとなります。 up_to_dateがfalseの場合、残高の集計が完了していません。最新の集計結果を確認したい場合は、時間を空けて再度取得する必要があります。 配賦仕訳の絞り込み（cost_allocation）は法人スタンダードプラン（および旧法人ベーシックプラン）以上で利用可能です。 partner_codeとpartner_idは同時に指定することはできません。 start_date / end_date を指定した場合、以下を同時に指定することはできません。 fiscal_year start_month end_month 0を指定すると未選択で絞り込めます partner_idに0を指定して...

### GET /api/1/reports/trial_pl_segment_1_tags

**操作**: 損益計算書(セグメント１比較)の取得

**説明**: 概要 指定した事業所の損益計算書(セグメント１比較)を取得する 定義 created_at : 作成日時 account_item_name : 勘定科目名 hierarchy_level: 階層レベル parent_account_category_name: 上位勘定科目カテゴリー名 closing_balance : 期末残高 注意点 会計年度が指定されない場合、現在の会計年度がデフォルトとなります。 up_to_dateがfalseの場合、残高の集計が完了していません。最新の集計結果を確認したい場合は、時間を空けて再度取得する必要があります。 配賦仕訳の絞り込み（cost_allocation）は法人スタンダードプラン（および旧法人ベーシックプラン）以上で利用可能です。 partner_codeとpartner_idは同時に指定することはできません。 start_date / end_date を指定した場合、以下を同時に指定することはできません。 fiscal_year start_month end_month 0を指定すると未選択で絞り込めます partner_idに0を...

### GET /api/1/reports/trial_pl_segment_2_tags

**操作**: 損益計算書(セグメント２比較)の取得

**説明**: 概要 指定した事業所の損益計算書(セグメント２比較)を取得する 定義 created_at : 作成日時 account_item_name : 勘定科目名 hierarchy_level: 階層レベル parent_account_category_name: 上位勘定科目カテゴリー名 closing_balance : 期末残高 注意点 会計年度が指定されない場合、現在の会計年度がデフォルトとなります。 up_to_dateがfalseの場合、残高の集計が完了していません。最新の集計結果を確認したい場合は、時間を空けて再度取得する必要があります。 配賦仕訳の絞り込み（cost_allocation）は法人スタンダードプラン（および旧法人ベーシックプラン）以上で利用可能です。 partner_codeとpartner_idは同時に指定することはできません。 start_date / end_date を指定した場合、以下を同時に指定することはできません。 fiscal_year start_month end_month 0を指定すると未選択で絞り込めます partner_idに0を...

### GET /api/1/reports/trial_pl_segment_3_tags

**操作**: 損益計算書(セグメント３比較)の取得

**説明**: 概要 指定した事業所の損益計算書(セグメント３比較)を取得する 定義 created_at : 作成日時 account_item_name : 勘定科目名 hierarchy_level: 階層レベル parent_account_category_name: 上位勘定科目カテゴリー名 closing_balance : 期末残高 注意点 会計年度が指定されない場合、現在の会計年度がデフォルトとなります。 up_to_dateがfalseの場合、残高の集計が完了していません。最新の集計結果を確認したい場合は、時間を空けて再度取得する必要があります。 配賦仕訳の絞り込み（cost_allocation）は法人スタンダードプラン（および旧法人ベーシックプラン）以上で利用可能です。 partner_codeとpartner_idは同時に指定することはできません。 start_date / end_date を指定した場合、以下を同時に指定することはできません。 fiscal_year start_month end_month 0を指定すると未選択で絞り込めます partner_idに0を...

### GET /api/1/reports/trial_cr

**操作**: 製造原価報告書の取得

**説明**: 概要 指定した事業所の製造原価報告書を取得する 定義 created_at : 作成日時 account_item_name : 勘定科目名 hierarchy_level: 階層レベル parent_account_category_name: 上位勘定科目カテゴリー名 opening_balance : 期首残高 debit_amount : 借方金額 credit_amount: 貸方金額 closing_balance : 期末残高 composition_ratio : 構成比 注意点 会計年度が指定されない場合、現在の会計年度がデフォルトとなります。 up_to_dateがfalseの場合、残高の集計が完了していません。最新の集計結果を確認したい場合は、時間を空けて再度取得する必要があります。 配賦仕訳の絞り込み（cost_allocation）は法人スタンダードプラン（および旧法人ベーシックプラン）以上で利用可能です。 partner_codeとpartner_idは同時に指定することはできません。 start_date / end_date を指定した場合、以下を同時に...

### GET /api/1/reports/trial_cr_two_years

**操作**: 製造原価報告書(前年比較)の取得

**説明**: 概要 指定した事業所の製造原価報告書(前年比較)を取得する 定義 created_at : 作成日時 account_item_name : 勘定科目名 hierarchy_level: 階層レベル parent_account_category_name: 上位勘定科目カテゴリー名 last_year_closing_balance: 前年度期末残高 closing_balance : 期末残高 year_on_year : 前年比 注意点 会計年度が指定されない場合、現在の会計年度がデフォルトとなります。 up_to_dateがfalseの場合、残高の集計が完了していません。最新の集計結果を確認したい場合は、時間を空けて再度取得する必要があります。 配賦仕訳の絞り込み（cost_allocation）は法人スタンダードプラン（および旧法人ベーシックプラン）以上で利用可能です。 partner_codeとpartner_idは同時に指定することはできません。 start_date / end_date を指定した場合、以下を同時に指定することはできません。 fiscal_year s...

### GET /api/1/reports/trial_cr_three_years

**操作**: 製造原価報告書(３期間比較)の取得

**説明**: 概要 指定した事業所の製造原価報告書(３期間比較)を取得する 定義 created_at : 作成日時 account_item_name : 勘定科目名 hierarchy_level: 階層レベル parent_account_category_name: 上位勘定科目カテゴリー名 two_years_before_closing_balance: 前々年度期末残高 last_year_closing_balance: 前年度期末残高 closing_balance : 期末残高 year_on_year : 前年比 注意点 会計年度が指定されない場合、現在の会計年度がデフォルトとなります。 up_to_dateがfalseの場合、残高の集計が完了していません。最新の集計結果を確認したい場合は、時間を空けて再度取得する必要があります。 配賦仕訳の絞り込み（cost_allocation）は法人スタンダードプラン（および旧法人ベーシックプラン）以上で利用可能です。 partner_codeとpartner_idは同時に指定することはできません。 start_date / end_da...

### GET /api/1/reports/trial_cr_sections

**操作**: 製造原価報告書(部門比較)の取得

**説明**: 概要 指定した事業所の製造原価報告書(部門比較)を取得する 定義 created_at : 作成日時 account_item_name : 勘定科目名 hierarchy_level: 階層レベル parent_account_category_name: 上位勘定科目カテゴリー名 closing_balance : 期末残高 注意点 会計年度が指定されない場合、現在の会計年度がデフォルトとなります。 up_to_dateがfalseの場合、残高の集計が完了していません。最新の集計結果を確認したい場合は、時間を空けて再度取得する必要があります。 配賦仕訳の絞り込み（cost_allocation）は法人スタンダードプラン（および旧法人ベーシックプラン）以上で利用可能です。 partner_codeとpartner_idは同時に指定することはできません。 start_date / end_date を指定した場合、以下を同時に指定することはできません。 fiscal_year start_month end_month 0を指定すると未選択で絞り込めます partner_idに0を指定...

### GET /api/1/reports/trial_cr_segment_1_tags

**操作**: 製造原価報告書(セグメント１比較)の取得

**説明**: 概要 指定した事業所の製造原価報告書(セグメント１比較)を取得する 定義 created_at : 作成日時 account_item_name : 勘定科目名 hierarchy_level: 階層レベル parent_account_category_name: 上位勘定科目カテゴリー名 closing_balance : 期末残高 注意点 会計年度が指定されない場合、現在の会計年度がデフォルトとなります。 up_to_dateがfalseの場合、残高の集計が完了していません。最新の集計結果を確認したい場合は、時間を空けて再度取得する必要があります。 partner_codeとpartner_idは同時に指定することはできません。 start_date / end_date を指定した場合、以下を同時に指定することはできません。 fiscal_year start_month end_month 0を指定すると未選択で絞り込めます partner_idに0を指定して絞り込んだ場合 取引先が設定されていない取引、振替伝票の金額がレスポンスに返却されます レスポンスの例 GET htt...

### GET /api/1/reports/trial_cr_segment_2_tags

**操作**: 製造原価報告書(セグメント２比較)の取得

**説明**: 概要 指定した事業所の製造原価報告書(セグメント２比較)を取得する 定義 created_at : 作成日時 account_item_name : 勘定科目名 hierarchy_level: 階層レベル parent_account_category_name: 上位勘定科目カテゴリー名 closing_balance : 期末残高 注意点 会計年度が指定されない場合、現在の会計年度がデフォルトとなります。 up_to_dateがfalseの場合、残高の集計が完了していません。最新の集計結果を確認したい場合は、時間を空けて再度取得する必要があります。 partner_codeとpartner_idは同時に指定することはできません。 start_date / end_date を指定した場合、以下を同時に指定することはできません。 fiscal_year start_month end_month 0を指定すると未選択で絞り込めます partner_idに0を指定して絞り込んだ場合 取引先が設定されていない取引、振替伝票の金額がレスポンスに返却されます レスポンスの例 GET htt...

### GET /api/1/reports/trial_cr_segment_3_tags

**操作**: 製造原価報告書(セグメント３比較)の取得

**説明**: 概要 指定した事業所の製造原価報告書(セグメント３比較)を取得する 定義 created_at : 作成日時 account_item_name : 勘定科目名 hierarchy_level: 階層レベル parent_account_category_name: 上位勘定科目カテゴリー名 closing_balance : 期末残高 注意点 会計年度が指定されない場合、現在の会計年度がデフォルトとなります。 up_to_dateがfalseの場合、残高の集計が完了していません。最新の集計結果を確認したい場合は、時間を空けて再度取得する必要があります。 partner_codeとpartner_idは同時に指定することはできません。 start_date / end_date を指定した場合、以下を同時に指定することはできません。 fiscal_year start_month end_month 0を指定すると未選択で絞り込めます partner_idに0を指定して絞り込んだ場合 取引先が設定されていない取引、振替伝票の金額がレスポンスに返却されます レスポンスの例 GET htt...



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [accounting-api-schema.json](../../openapi/accounting-api-schema.json)
