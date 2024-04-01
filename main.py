from fastapi import FastAPI, Query
from typing import Annotated
# python -m uvicorn main:app --reloadで起動

app = FastAPI()

# 1
@app.get("/user/{user_id}")
def read_user(user_id):
  return {
    "user_id": user_id,
    "name": "山田 太郎",
    "department": "営業部",
    "office": "東京本社"
  }

# 2
@app.get("/ledger")
def read_ledger():
  return {
    "ledger_id": 21,
    "ledger_name": "確認書"
  }

items = ["Tシャツ", "スカート", "ブーツ", "コート"]

# 3
# (補足)ge=以上、le=以下、gt=より大きい、lt=より小さい
@app.get("/items")
def read_item(skip: int = 0, limit: Annotated[int, Query(ge=1, le=10)] = 10):
  return {"items": items[skip : skip + limit]}

# 4
@app.get("/items/{item_id}")
def read_item(
  item_id: str,
  skip: int = 0,
  limit: Annotated[int, Query(ge=1, le=10)] = 10
):
  return {"items": items[skip : skip + limit], "item_id": item_id}
