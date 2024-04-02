from fastapi import FastAPI, Query
from typing import Annotated
# python -m uvicorn main:appで起動

app = FastAPI()

# ユーザー情報
@app.get("/user/{user_id}")
def read_user(user_id):
  return {
    "user_id": user_id,
    "name": "山田 太郎",
    "department": "営業部",
    "office": "東京本社"
  }

# 帳票データ
@app.get("/ledger")
def read_ledger():
  return [
    {
      "name": "Frozen Yogurt",
      "calories": 159,
      "fat": 6.0,
      "carbs": 24,
      "protein": 4.0,
      "iron": "1",
    },
    {
      "name": "Jelly bean",
      "calories": 375,
      "fat": 0.0,
      "carbs": 94,
      "protein": 0.0,
      "iron": "0",
    },
    {
      "name": "KitKat",
      "calories": 518,
      "fat": 26.0,
      "carbs": 65,
      "protein": 7,
      "iron": "5",
    },
    {
      "name": "Eclair",
      "calories": 262,
      "fat": 16.0,
      "carbs": 23,
      "protein": 6.0,
      "iron": "11",
    },
    {
      "name": "Gingerbread",
      "calories": 356,
      "fat": 16.0,
      "carbs": 49,
      "protein": 3.9,
      "iron": "6",
    },
    {
      "name": "Ice cream sandwich",
      "calories": 237,
      "fat": 9.0,
      "carbs": 37,
      "protein": 4.3,
      "iron": "1",
    },
    {
      "name": "Lollipop",
      "calories": 392,
      "fat": 0.2,
      "carbs": 98,
      "protein": 0,
      "iron": "2",
    },
    {
      "name": "Cupcake",
      "calories": 305,
      "fat": 3.7,
      "carbs": 67,
      "protein": 4.3,
      "iron": "8",
    },
    {
      "name": "Honeycomb",
      "calories": 408,
      "fat": 3.2,
      "carbs": 87,
      "protein": 6.5,
      "iron": "45",
    },
    {
      "name": "Donut",
      "calories": 452,
      "fat": 25.0,
      "carbs": 51,
      "protein": 4.9,
      "iron": "2",
    },
    {
      "name": "Lollipop",
      "calories": 392,
      "fat": 0.2,
      "carbs": 98,
      "protein": 0,
      "iron": "2",
    },
    {
      "name": "Cupcake",
      "calories": 305,
      "fat": 3.7,
      "carbs": 67,
      "protein": 4.3,
      "iron": "8",
    },
    {
      "name": "Honeycomb",
      "calories": 408,
      "fat": 3.2,
      "carbs": 87,
      "protein": 6.5,
      "iron": "45",
    },
    {
      "name": "Donut",
      "calories": 452,
      "fat": 25.0,
      "carbs": 51,
      "protein": 4.9,
      "iron": "2",
    },
    {
      "name": "Lollipop",
      "calories": 392,
      "fat": 0.2,
      "carbs": 98,
      "protein": 0,
      "iron": "2",
    },
    {
      "name": "Cupcake",
      "calories": 305,
      "fat": 3.7,
      "carbs": 67,
      "protein": 4.3,
      "iron": "8",
    },
    {
      "name": "Honeycomb",
      "calories": 408,
      "fat": 3.2,
      "carbs": 87,
      "protein": 6.5,
      "iron": "45",
    },
    {
      "name": "Donut",
      "calories": 452,
      "fat": 25.0,
      "carbs": 51,
      "protein": 4.9,
      "iron": "2",
    },
    {
      "name": "Lollipop",
      "calories": 392,
      "fat": 0.2,
      "carbs": 98,
      "protein": 0,
      "iron": "2",
    },
    {
      "name": "Cupcake",
      "calories": 305,
      "fat": 3.7,
      "carbs": 67,
      "protein": 4.3,
      "iron": "8",
    },
    {
      "name": "Honeycomb",
      "calories": 408,
      "fat": 3.2,
      "carbs": 87,
      "protein": 6.5,
      "iron": "45",
    },
    {
      "name": "Donut",
      "calories": 452,
      "fat": 25.0,
      "carbs": 51,
      "protein": 4.9,
      "iron": "2",
    },
    {
      "name": "Lollipop",
      "calories": 392,
      "fat": 0.2,
      "carbs": 98,
      "protein": 0,
      "iron": "2",
    },
    {
      "name": "Cupcake",
      "calories": 305,
      "fat": 3.7,
      "carbs": 67,
      "protein": 4.3,
      "iron": "8",
    },
    {
      "name": "Honeycomb",
      "calories": 408,
      "fat": 3.2,
      "carbs": 87,
      "protein": 6.5,
      "iron": "45",
    },
    {
      "name": "Donut",
      "calories": 452,
      "fat": 25.0,
      "carbs": 51,
      "protein": 4.9,
      "iron": "2",
    },
    {
      "name": "Lollipop",
      "calories": 392,
      "fat": 0.2,
      "carbs": 98,
      "protein": 0,
      "iron": "2",
    },
    {
      "name": "Cupcake",
      "calories": 305,
      "fat": 3.7,
      "carbs": 67,
      "protein": 4.3,
      "iron": "8",
    },
    {
      "name": "Honeycomb",
      "calories": 408,
      "fat": 3.2,
      "carbs": 87,
      "protein": 6.5,
      "iron": "45",
    },
    {
      "name": "Donut",
      "calories": 452,
      "fat": 25.0,
      "carbs": 51,
      "protein": 4.9,
      "iron": "2",
    },
    {
      "name": "Lollipop",
      "calories": 392,
      "fat": 0.2,
      "carbs": 98,
      "protein": 0,
      "iron": "2",
    },
    {
      "name": "Cupcake",
      "calories": 305,
      "fat": 3.7,
      "carbs": 67,
      "protein": 4.3,
      "iron": "8",
    },
    {
      "name": "Honeycomb",
      "calories": 408,
      "fat": 3.2,
      "carbs": 87,
      "protein": 6.5,
      "iron": "45",
    },
    {
      "name": "Donut",
      "calories": 452,
      "fat": 25.0,
      "carbs": 51,
      "protein": 4.9,
      "iron": "2",
    },
    {
      "name": "Lollipop",
      "calories": 392,
      "fat": 0.2,
      "carbs": 98,
      "protein": 0,
      "iron": "2",
    },
    {
      "name": "Cupcake",
      "calories": 305,
      "fat": 3.7,
      "carbs": 67,
      "protein": 4.3,
      "iron": "8",
    },
    {
      "name": "Honeycomb",
      "calories": 408,
      "fat": 3.2,
      "carbs": 87,
      "protein": 6.5,
      "iron": "45",
    },
    {
      "name": "Donut",
      "calories": 452,
      "fat": 25.0,
      "carbs": 51,
      "protein": 4.9,
      "iron": "2",
    },
    {
      "name": "Lollipop",
      "calories": 392,
      "fat": 0.2,
      "carbs": 98,
      "protein": 0,
      "iron": "2",
    },
    {
      "name": "Cupcake",
      "calories": 305,
      "fat": 3.7,
      "carbs": 67,
      "protein": 4.3,
      "iron": "8",
    },
    {
      "name": "Honeycomb",
      "calories": 408,
      "fat": 3.2,
      "carbs": 87,
      "protein": 6.5,
      "iron": "45",
    },
    {
      "name": "Donut",
      "calories": 452,
      "fat": 25.0,
      "carbs": 51,
      "protein": 4.9,
      "iron": "2",
    },
    {
      "name": "Lollipop",
      "calories": 392,
      "fat": 0.2,
      "carbs": 98,
      "protein": 0,
      "iron": "2",
    },
    {
      "name": "Cupcake",
      "calories": 305,
      "fat": 3.7,
      "carbs": 67,
      "protein": 4.3,
      "iron": "8",
    },
    {
      "name": "Honeycomb",
      "calories": 408,
      "fat": 3.2,
      "carbs": 87,
      "protein": 6.5,
      "iron": "45",
    },
    {
      "name": "Donut",
      "calories": 452,
      "fat": 25.0,
      "carbs": 51,
      "protein": 4.9,
      "iron": "2",
    },
    {
      "name": "Lollipop",
      "calories": 392,
      "fat": 0.2,
      "carbs": 98,
      "protein": 0,
      "iron": "2",
    },
    {
      "name": "Cupcake",
      "calories": 305,
      "fat": 3.7,
      "carbs": 67,
      "protein": 4.3,
      "iron": "8",
    },
    {
      "name": "Honeycomb",
      "calories": 408,
      "fat": 3.2,
      "carbs": 87,
      "protein": 6.5,
      "iron": "45",
    },
    {
      "name": "Donut",
      "calories": 452,
      "fat": 25.0,
      "carbs": 51,
      "protein": 4.9,
      "iron": "2",
    },
    {
      "name": "Lollipop",
      "calories": 392,
      "fat": 0.2,
      "carbs": 98,
      "protein": 0,
      "iron": "2",
    },
    {
      "name": "Cupcake",
      "calories": 305,
      "fat": 3.7,
      "carbs": 67,
      "protein": 4.3,
      "iron": "8",
    },
    {
      "name": "Honeycomb",
      "calories": 408,
      "fat": 3.2,
      "carbs": 87,
      "protein": 6.5,
      "iron": "45",
    },
    {
      "name": "Donut",
      "calories": 452,
      "fat": 25.0,
      "carbs": 51,
      "protein": 4.9,
      "iron": "2",
    },
    {
      "name": "Lollipop",
      "calories": 392,
      "fat": 0.2,
      "carbs": 98,
      "protein": 0,
      "iron": "2",
    },
    {
      "name": "Cupcake",
      "calories": 305,
      "fat": 3.7,
      "carbs": 67,
      "protein": 4.3,
      "iron": "8",
    },
    {
      "name": "Honeycomb",
      "calories": 408,
      "fat": 3.2,
      "carbs": 87,
      "protein": 6.5,
      "iron": "45",
    },
    {
      "name": "Donut",
      "calories": 452,
      "fat": 25.0,
      "carbs": 51,
      "protein": 4.9,
      "iron": "2",
    },
    {
      "name": "Lollipop",
      "calories": 392,
      "fat": 0.2,
      "carbs": 98,
      "protein": 0,
      "iron": "2",
    },
    {
      "name": "Cupcake",
      "calories": 305,
      "fat": 3.7,
      "carbs": 67,
      "protein": 4.3,
      "iron": "8",
    },
    {
      "name": "Honeycomb",
      "calories": 408,
      "fat": 3.2,
      "carbs": 87,
      "protein": 6.5,
      "iron": "45",
    },
    {
      "name": "Donut",
      "calories": 452,
      "fat": 25.0,
      "carbs": 51,
      "protein": 4.9,
      "iron": "2",
    },
    {
      "name": "Lollipop",
      "calories": 392,
      "fat": 0.2,
      "carbs": 98,
      "protein": 0,
      "iron": "2",
    },
    {
      "name": "Cupcake",
      "calories": 305,
      "fat": 3.7,
      "carbs": 67,
      "protein": 4.3,
      "iron": "8",
    },
    {
      "name": "Honeycomb",
      "calories": 408,
      "fat": 3.2,
      "carbs": 87,
      "protein": 6.5,
      "iron": "45",
    },
    {
      "name": "Donut",
      "calories": 452,
      "fat": 25.0,
      "carbs": 51,
      "protein": 4.9,
      "iron": "2",
    },
    {
      "name": "Lollipop",
      "calories": 392,
      "fat": 0.2,
      "carbs": 98,
      "protein": 0,
      "iron": "2",
    },
    {
      "name": "Cupcake",
      "calories": 305,
      "fat": 3.7,
      "carbs": 67,
      "protein": 4.3,
      "iron": "8",
    },
    {
      "name": "Honeycomb",
      "calories": 408,
      "fat": 3.2,
      "carbs": 87,
      "protein": 6.5,
      "iron": "45",
    },
    {
      "name": "Donut",
      "calories": 452,
      "fat": 25.0,
      "carbs": 51,
      "protein": 4.9,
      "iron": "2",
    },
    {
      "name": "Lollipop",
      "calories": 392,
      "fat": 0.2,
      "carbs": 98,
      "protein": 0,
      "iron": "2",
    },
    {
      "name": "Cupcake",
      "calories": 305,
      "fat": 3.7,
      "carbs": 67,
      "protein": 4.3,
      "iron": "8",
    },
    {
      "name": "Honeycomb",
      "calories": 408,
      "fat": 3.2,
      "carbs": 87,
      "protein": 6.5,
      "iron": "45",
    },
    {
      "name": "Donut",
      "calories": 452,
      "fat": 25.0,
      "carbs": 51,
      "protein": 4.9,
      "iron": "2",
    },
    {
      "name": "Lollipop",
      "calories": 392,
      "fat": 0.2,
      "carbs": 98,
      "protein": 0,
      "iron": "2",
    },
    {
      "name": "Cupcake",
      "calories": 305,
      "fat": 3.7,
      "carbs": 67,
      "protein": 4.3,
      "iron": "8",
    },
    {
      "name": "Honeycomb",
      "calories": 408,
      "fat": 3.2,
      "carbs": 87,
      "protein": 6.5,
      "iron": "45",
    },
    {
      "name": "Donut",
      "calories": 452,
      "fat": 25.0,
      "carbs": 51,
      "protein": 4.9,
      "iron": "2",
    },
    {
      "name": "Donut2",
      "calories": 452,
      "fat": 25.0,
      "carbs": 51,
      "protein": 4.9,
      "iron": "2",
    }
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



offices = ["北海道営業所", "青森本社", "秋田営業所", "東京営業所", "愛知営業所", "大坂営業所", "兵庫営業所", "福岡営業所"]

# 事業所名
@app.get("/office")
def read_office():
  return {"office": offices}

# 部署名
@app.get("/department")
def read_department():
    departments = []
    for office in offices:
        departments.extend([
            {office: "第一営業部"},
            {office: "管理部"},
            {office: "第二営業部"},
            {office: "人事部"}
        ])
    return departments
