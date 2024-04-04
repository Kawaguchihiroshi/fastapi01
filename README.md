# テスト用API
ローカルで気軽に確認できるようにデータベースを絡めないテスト用API

## 動作環境
Python 3.11.8
バージョン確認
```
$ python --version
```
**インストール（windows）**；https://www.python.org/downloads/windows/
**インストール（mac）**；https://www.python.org/downloads/macos/

pipのアップグレード
```
$ python -m pip install --upgrade pip
```

FastAPIをインストール
```
$ pip install fastapi
```

Uvicornをインストール
```
$ pip install "uvicorn[standard]"
```

Requestsのインストール
```
$ pip install requests
```

## main.py
エンドポイント設定用ファイル
###### 実行コマンド
python -m uvicorn main:app

## client.py
main.py側がちゃんと動作しているか確認用のファイル
###### 実行コマンド
python .\client.py
