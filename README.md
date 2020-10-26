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
4. srcやcommandと同じ階層にlogin_info/login.jsonを作成し、以下の内容を記入.
```
{
    "username":"AtCoderのユーザーネーム",
    "password":"AtCoderのパスワード"
}
```

## 実行方法
1. ターミナルを起動し, 問題を解答となるスクリプトがあるDirectoryに移動する.  
  
2. 問題を解く前に以下のコマンドを実行して, テストケースを手元にスクレイピングしておく.実行すると./casesが作成され、そこにテストケースが格納される.
```
aat s コンテスト名
```
- 例
```
aat s ABC150
```
3. 問題を解く.スクリプトはABC150A.pyのように,コンテスト名+問題番号という名前で保存しておく.  
  
4. 問題が解けたら,以下のコマンドを実行してテストケースに通るか確認する.
```
aat p コンテスト名 問題番号
```
- 例
```
aat p ABC150 A
```
5. テストケースを全て通過すれば,以下のようなメッセージが表示される.
```
excute mode
Passed all test cases!
```
6. もし、通らないテストケースがあった場合は、以下のようなメッセージが表示される.
```
excute mode
Failed: 1 
Input: 4 10
Expected: 3
Actual:   4
Failed: 3
Input: 8 8
Expected: 1
Actual:   2
```
```
Failed: 通らなかったテストケースの番号  
  
Input: テストケースの入力  
  
Expected: 想定していた出力  
  
Actual: 実際の出力  
```
