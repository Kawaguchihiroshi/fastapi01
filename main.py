from fastapi import FastAPI, Query
from typing import Annotated
from typing import Union
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# python -m uvicorn main:appで起動

app = FastAPI()

# ユーザー情報（全員）
@app.get("/user")
def read_user():
  return [
     {
      "user_id": "ABC001001",
      "user_name": "山田 太郎",
      "department_id": "e001",
      "department_name": "第一営業部",
      "office_id": "off0001",
      "office_name": "東京本社"
    },
    {
      "user_id": "ABC001002",
      "user_name": "山田 次郎",
      "department_id": "e002",
      "department_name": "第二営業部",
      "office_id": "off0001",
      "office_name": "東京本社"
    },
    {
      "user_id": "ABC001003",
      "user_name": "山田 三郎",
      "department_id": "e001",
      "department_name": "第一営業部",
      "office_id": "off0002",
      "office_name": "大阪営業所"
    },
  ]

# ユーザー情報（個人）
@app.get("/user/{user_id}")
def read_user(user_id):
  return {
    "user_id": user_id,
    "user_name": "山田 太郎",
    "department_id": "e001",
    "department_name": "営業部",
    "office_id": "off0001",
    "office_name": "東京本社"
  }


# 帳票データ
@app.get("/ledger")
def read_ledger():
  return [
    {
      "case_id": "cid0101001",
      "case_name": "東京スカイツリー",
      "handle_id": "hid0101001",
      "handle_name": "山田太郎",
      "user_id": "ABC001001",
      "department_id": "did001",
      "department_name": "営業部",
      "office_id": "oid0001",
      "office_name": "東京本社",
      "status_id": "sid004",
      "status_name": "確認済み",
      "created_at": 20240101,
      "confirmation_at": 20240115
    },
    {
      "case_id": "cid0101001",
      "case_name": "東京スカイツリー",
      "handle_id": "hid0101001",
      "handle_name": "山田太郎",
      "user_id": "ABC001001",
      "department_id": "did001",
      "department_name": "営業部",
      "office_id": "oid0001",
      "office_name": "東京本社",
      "status_id": "sid004",
      "status_name": "確認済み",
      "created_at": 20240101,
      "confirmation_at": 20240115
    },
    {
      "case_id": "cid0101001",
      "case_name": "東京スカイツリー",
      "handle_id": "hid0101001",
      "handle_name": "山田太郎",
      "user_id": "ABC001001",
      "department_id": "did001",
      "department_name": "営業部",
      "office_id": "oid0001",
      "office_name": "東京本社",
      "status_id": "sid004",
      "status_name": "確認済み",
      "created_at": 20240101,
      "confirmation_at": 20240115
    },
    {
      "case_id": "cid0101001",
      "case_name": "東京スカイツリー",
      "handle_id": "hid0101001",
      "handle_name": "山田太郎",
      "user_id": "ABC001001",
      "department_id": "did001",
      "department_name": "営業部",
      "office_id": "oid0001",
      "office_name": "東京本社",
      "status_id": "sid004",
      "status_name": "確認済み",
      "created_at": 20240101,
      "confirmation_at": 20240115
    },
  ]



# items = ["北海道", "青森県", "秋田県", "岩手県"]

# 3
# (補足)ge=以上、le=以下、gt=より大きい、lt=より小さい
# @app.get("/items")
# def read_item(skip: int = 0, limit: Annotated[int, Query(ge=1, le=10)] = 10):
#   return {"items": items[skip : skip + limit]}

# 4
# @app.get("/items/{item_id}")
# def read_item(
#   item_id: str,
#   skip: int = 0,
#   limit: Annotated[int, Query(ge=1, le=10)] = 10
# ):
#   return {"items": items[skip : skip + limit], "item_id": item_id}


offices = [
  {
    "office_id": "oid0001",
    "office_name": "東京営業所",
  },
  {
    "office_id": "oid0002",
    "office_name": "北海道営業所",
  },
  {
    "office_id": "oid0003",
    "office_name": "青森本社",
  },
  {
    "office_id": "oid0004",
    "office_name": "秋田営業所",
  },
  {
    "office_id": "oid0005",
    "office_name": "愛知営業所",
  },
  {
    "office_id": "oid0006",
    "office_name": "大阪営業所",
  },
  {
    "office_id": "oid0007",
    "office_name": "兵庫営業所",
  },
  {
    "office_id": "oid0008",
    "office_name": "福岡営業所",
  },
]
# 事業所名
@app.get("/office")
def read_office():
  return offices



departments = [
  {
    "office_id": "oid0001",
    "office_name": "東京営業所",
    "department_id": "did0101",
    "department_name": "第一営業部",
  },
  {
    "office_id": "oid0001",
    "office_name": "東京営業所",
    "department_id": "did0102",
    "department_name": "第二営業部",
  },
  {
    "office_id": "oid0001",
    "office_name": "東京営業所",
    "department_id": "did0103",
    "department_name": "営業管理部",
  },
  {
    "office_id": "oid0002",
    "office_name": "北海道営業所",
    "department_id": "did0201",
    "department_name": "営業部",
  },
  {
    "office_id": "oid0002",
    "office_name": "北海道営業所",
    "department_id": "did0202",
    "department_name": "営業管理部",
  },
  {
    "office_id": "oid0003",
    "office_name": "青森本社",
    "department_id": "did0301",
    "department_name": "第一営業部",
  },
  {
    "office_id": "oid0003",
    "office_name": "青森本社",
    "department_id": "did0302",
    "department_name": "第二営業部",
  },
  {
    "office_id": "oid0003",
    "office_name": "青森本社",
    "department_id": "did0303",
    "department_name": "営業管理部",
  },
  {
    "office_id": "oid0004",
    "office_name": "秋田営業所",
    "department_id": "did0401",
    "department_name": "営業部",
  },
  {
    "office_id": "oid0004",
    "office_name": "秋田営業所",
    "department_id": "did0402",
    "department_name": "営業管理部",
  },
  {
    "office_id": "oid0005",
    "office_name": "愛知営業所",
    "department_id": "did0501",
    "department_name": "第一営業部",
  },
  {
    "office_id": "oid0005",
    "office_name": "愛知営業所",
    "department_id": "did0502",
    "department_name": "第二営業部",
  },
  {
    "office_id": "oid0005",
    "office_name": "愛知営業所",
    "department_id": "did0503",
    "department_name": "営業管理部",
  },
  {
    "office_id": "oid0006",
    "office_name": "大阪営業所",
    "department_id": "did0601",
    "department_name": "営業部",
  },
  {
    "office_id": "oid0006",
    "office_name": "大阪営業所",
    "department_id": "did0602",
    "department_name": "営業管理部",
  },
  {
    "office_id": "oid0007",
    "office_name": "兵庫営業所",
    "department_id": "did0701",
    "department_name": "第一営業部",
  },
  {
    "office_id": "oid0007",
    "office_name": "兵庫営業所",
    "department_id": "did0702",
    "department_name": "第二営業部",
  },
  {
    "office_id": "oid0007",
    "office_name": "兵庫営業所",
    "department_id": "did0703",
    "department_name": "営業管理部",
  },
  {
    "office_id": "oid0008",
    "office_name": "福岡営業所",
    "department_id": "did0801",
    "department_name": "営業部",
  },
  {
    "office_id": "oid0008",
    "office_name": "福岡営業所",
    "department_id": "did0802",
    "department_name": "営業管理部",
  },
]
# 部署名
@app.get("/department")
def read_department():
  return departments

# handles = [
#   {}
# ]

# 担当者名
# @app.get("/department")
# def read_handle():
#   return handles


# 確認書の新規登録
# class Item(BaseModel):
#   name: str
#   price: float
#   description: Union[str, None] = None

# @app.post("/newitems/")
# def create_item(item: Item):
#   print(f"データを登録します: {item.name}, {item.price}, {item.description}")
#   return item

# CORSミドルウェアを追加してOPTIONSメソッドを許可する
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # すべてのオリジンを許可（必要に応じて適切な設定に変更）
    allow_methods=["*"],  # すべてのHTTPメソッドを許可（必要に応じて適切な設定に変更）
    allow_headers=["*"],  # すべてのヘッダーを許可（必要に応じて適切な設定に変更）
)


# ユーザーの新規登録
class User(BaseModel):
  name: str
  mail: str
  description: Union[str, None] = None

@app.post("/newusers")
def create_user(user: User):
  print(f"データを登録します: {user.name}, {user.mail}, {user.description}")
  return user
