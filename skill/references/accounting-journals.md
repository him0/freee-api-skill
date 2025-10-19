# Journals

## 概要

仕訳帳

## エンドポイント一覧

### GET /api/1/journals

**操作**: 仕訳帳のダウンロード要求

**説明**: 概要 ユーザーが所属する事業所の仕訳帳のダウンロードをリクエストします。 生成されるファイルのファイル形式と出力項目に関しては、ヘルプページをご参照ください。 定義 download_type generic (旧CSV) generic_v2 (新CSV（freee汎用形式）) csv (弥生会計) pdf (PDF) encoding : download_typeがgeneric, generic_v2の場合のみ有効で、指定しない場合はsjisになります。無効なdownload_typeのうちcsvの場合はsjisでファイル出力されるので、レスポンスでsjisがかえります。 sjis utf-8 visible_tags : download_typeがgeneric, csv, pdfの場合のみ有効です。指定しない場合は従来の仕様の仕訳帳が出力されます。 partner : 取引先タグ item : 品目タグ tag : メモタグ section : 部門タグ description : 備考欄 wallet_txn_description : 明細の備考欄 segment_1...

### GET /api/1/journals/reports/{id}/status

**操作**: 仕訳帳のステータスの取得

**説明**: 概要 仕訳帳のダウンロードリクエストのステータスを取得する 定義 status enqueued : 実行待ち working : 実行中 uploaded : 準備完了 id : 受け付けID

### GET /api/1/journals/reports/{id}/download

**操作**: 仕訳帳のダウンロード

**説明**: 概要 仕訳帳をダウンロードする 定義 id : 受け付けID



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [accounting-api-schema.json](../../openapi/accounting-api-schema.json)
