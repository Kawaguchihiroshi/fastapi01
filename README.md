# テスト用API
ローカルで気軽に確認できるようにデータベースを絡めないテスト用API

## 動作環境
Python 3.11.8
バージョン確認
```
$ python --version
```
**インストール（windows）**；https://www.python.org/downloads/windows/<br>
**インストール（mac）**；https://www.python.org/downloads/macos/<br>
<br>
pipのアップグレード
```
$ python -m pip install --upgrade pip
```
<br><br>
FastAPIをインストール
```
$ pip install fastapi
```
<br><br>
Uvicornをインストール
```
$ pip install "uvicorn[standard]"
```
<br><br>
Requestsのインストール
```
$ pip install requests
```
<br><br>
## main.py
エンドポイント設定用ファイル
###### 実行コマンド
```
$ python -m uvicorn main:app
```
<br><br>
## client.py
main.py側がちゃんと動作しているか確認用のファイル
###### 実行コマンド
```
$ python .\client.py
```
