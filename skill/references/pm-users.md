# Users

## 概要

ログインユーザー

## エンドポイント一覧

### GET /users/me

**操作**: ログインユーザー情報の取得

**説明**: このリクエストの認可セッションにおけるログインユーザーの情報を返します。 freee工数管理では一人のログインユーザーを複数の事業所に関連付けられるため、このユーザーと関連のあるすべての事業所の情報をリストで返します。 他のAPIのパラメータとして company_id が求められる場合は、このAPIで取得した company_id を使用します。



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [pm-api-schema.json](../../openapi/pm-api-schema.json)
