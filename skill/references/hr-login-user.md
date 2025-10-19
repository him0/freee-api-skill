# ログインユーザー

## 概要

ログインユーザーの取得

## エンドポイント一覧

### GET /api/v1/users/me

**操作**: ログインユーザーの取得

**説明**: 概要 このリクエストの認可セッションにおけるログインユーザーの情報を返します。 freee人事労務では一人のログインユーザーを複数の事業所に関連付けられるため、このユーザーと関連のあるすべての事業所の情報をリストで返します。 注意点 他のAPIのパラメータとしてcompany_idが求められる場合は、このAPIで取得したcompany_idを使用します。 給与計算対象外の従業員のemployee_idとdisplay_nameは取得できません。



## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [hr-api-schema.json](../../openapi/hr-api-schema.json)
