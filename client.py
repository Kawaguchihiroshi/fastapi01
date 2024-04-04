import requests
# python .\client.pyで起動

# 1
res1 = requests.get("http://127.0.0.1:8000/user/0021")

# 2
res2 = requests.get("http://127.0.0.1:8000/ledger")

# 3
# res3 = requests.get("http://127.0.0.1:8000/items?skip=1&limit=2")

# 4
# res4 = requests.get("http://127.0.0.1:8000/items/main001?skip=1&limit=2")

# 5
res5 = requests.post("http://127.0.0.1:8000/newusers",json={'name': 'aaa','mail': 'aaa','description': 'aaa',})

print(res1.status_code)
print(res1.text)
print(res2.status_code)
print(res2.text)
# print(res3.status_code)
# print(res3.text)
# print(res4.status_code)
# print(res4.text)
print(res5.status_code)
print(res5.text)
