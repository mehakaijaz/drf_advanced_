import requests

endpoints='http://127.0.0.1:8000/api/products/1/'

get_response=requests.get(endpoints,json={"title":"new there","content": "Hello world", "price": "134"})

print(get_response.json())
print(get_response.status_code)