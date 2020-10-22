# AtcoderAutoTest
- AtCoderで自動でテストケースを実行するスクリプト.

# 使い方
## 準備
1. 適当な場所に本リポジトリをcloneする.
2. commandのpathを通す.例えばzshを使っている場合は以下のを~/.zshrcに追加する. (本リポジトリをDocuments以下に置いたと想定)
```
export PATH=$HOME/Documents/AtcoderAutoTest/command:$PATH
```
3. command/aatに実行権限を付与
```
chmod 755 ./command/aat
```
3. srcやcommandと同じ階層にlogin_info/login.jsonを作成し、以下の内容を記入.
```
{
    "username":"AtCoderのユーザーネーム",
    "password":"AtCoderのパスワード"
}
```

## 実行方法
