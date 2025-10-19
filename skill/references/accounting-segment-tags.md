# Segment tags

## 概要

セグメントタグ

## エンドポイント一覧

### GET /api/1/segments/{segment_id}/tags

**操作**: セグメントタグ一覧の取得

**説明**: 概要 指定した事業所のセグメントタグ一覧を取得する 注意点 事業所の設定でセグメントタグコードを使用する設定にしている場合、レスポンスでセグメントタグコード(code)を返します

### POST /api/1/segments/{segment_id}/tags

**操作**: セグメントタグの作成

**説明**: 概要 指定した事業所のセグメントタグを作成する 注意点 codeを利用するには、事業所の設定でセグメントタグコードを使用する設定にする必要があります。

### PUT /api/1/segments/{segment_id}/tags/{id}

**操作**: セグメントタグの更新

**説明**: 概要 指定した事業所のセグメントタグを更新する 注意点 codeを利用するには、事業所の設定でセグメントタグコードを使用する設定にする必要があります。

### DELETE /api/1/segments/{segment_id}/tags/{id}

**操作**: セグメントタグの削除

**説明**: 概要 指定した事業所のセグメントタグを削除する

### PUT /api/1/segments/{segment_id}/tags/code/upsert

**操作**: セグメントタグの更新（作成）

**説明**: 概要 セグメントタグコードをキーに、指定したセグメントタグの情報を更新（存在しない場合は作成）する 注意点 codeを利用するには、事業所の設定でセグメントタグコードを使用する設定にする必要があります。



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [accounting-api-schema.json](../../openapi/accounting-api-schema.json)
