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
使い方：https://fastapi.tiangolo.com/ja/
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
使い方：https://note.nkmk.me/python-requests-usage/
<br><br>
## main.py
エンドポイント設定用ファイル
###### 実行コマンド
```
$ python -m uvicorn main:app
```
<br><br>
## client.py
main.pyが正しく動作しているか確認するためのファイル
###### 実行コマンド
```
$ python .\client.py
```
