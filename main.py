from fastapi import FastAPI, Query
from typing import Annotated
from typing import Union
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# python -m uvicorn main:appで起動

app = FastAPI()

# CORSミドルウェアを追加してOPTIONSメソッドを許可する
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # すべてのオリジンを許可（必要に応じて適切な設定に変更）
    allow_methods=["*"],  # すべてのHTTPメソッドを許可（必要に応じて適切な設定に変更）
    allow_headers=["*"],  # すべてのヘッダーを許可（必要に応じて適切な設定に変更）
)



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
      "case_id": "cid0101002",
      "case_name": "隅田川",
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
      "case_id": "cid0101003",
      "case_name": "東京ディズニーランド",
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
      "case_id": "cid0101004",
      "case_name": "東京タワー",
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
      "case_id": "cid0101005",
      "case_name": "宮下パーク",
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
      "case_id": "cid0101006",
      "case_name": "スターバックス六本木店",
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
      "case_id": "cid0101007",
      "case_name": "後楽園",
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
      "case_id": "cid0101008",
      "case_name": "井之頭公園",
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

handles = [
  {
    "office_id": "oid0001",
    "office_name": "東京営業所",
    "department_id": "did0101",
    "department_name": "第一営業部",
    "handle_id": "hid0101001",
    "handle_name": "山田太郎",
  },
  {
    "office_id": "oid0001",
    "office_name": "東京営業所",
    "department_id": "did0101",
    "department_name": "第一営業部",
    "handle_id": "hid0101002",
    "handle_name": "山田次郎",
  },
  {
    "office_id": "oid0001",
    "office_name": "東京営業所",
    "department_id": "did0101",
    "department_name": "第一営業部",
    "handle_id": "hid0101003",
    "handle_name": "山田花美",
  },
  {
    "office_id": "oid0001",
    "office_name": "東京営業所",
    "department_id": "did0101",
    "department_name": "第一営業部",
    "handle_id": "hid0101004",
    "handle_name": "山田三郎",
  },
  {
    "office_id": "oid0001",
    "office_name": "東京営業所",
    "department_id": "did0102",
    "department_name": "第二営業部",
    "handle_id": "hid0102001",
    "handle_name": "多田太郎",
  },
  {
    "office_id": "oid0001",
    "office_name": "東京営業所",
    "department_id": "did0102",
    "department_name": "第二営業部",
    "handle_id": "hid0102002",
    "handle_name": "多田次郎",
  },
  {
    "office_id": "oid0001",
    "office_name": "東京営業所",
    "department_id": "did0102",
    "department_name": "第二営業部",
    "handle_id": "hid0102003",
    "handle_name": "多田花子",
  },
  {
    "office_id": "oid0001",
    "office_name": "東京営業所",
    "department_id": "did0103",
    "department_name": "営業管理部",
    "handle_id": "hid0103001",
    "handle_name": "山元太郎",
  },
  {
    "office_id": "oid0001",
    "office_name": "東京営業所",
    "department_id": "did0103",
    "department_name": "営業管理部",
    "handle_id": "hid0103002",
    "handle_name": "山元次郎",
  },
]

# 担当者名
@app.get("/handle")
def read_handle():
  return handles


# 確認書の新規登録
class Ledger(BaseModel):
  case_id: str
  case_name: str
  handle_id: str
  handle_name: str
  user_id: str
  department_id: str
  department_name: str
  office_id: str
  office_name: str
  status_id: str
  status_name: str
  created_at: int
  confirmation_at: int

@app.post("/newledger")
def create_ledger(ledger: Ledger):
  print(f"データを登録します: {ledger.case_name}, {ledger.handle_name}, {ledger.status_name}")
  return ledger



# 利用者の新規登録
class User(BaseModel):
  name: str
  mail: str
  select: str
  checkagree: bool

@app.post("/newuser")
def create_user(user: User):
  print(f"データを登録します: {user.name}, {user.mail}, {user.select}, {user.checkagree}")
  return user
