import requests

endpoints='http://127.0.0.1:8000/api/products/1/update/'
data={
    "title":"my old friend",
    'price':1234,"content":"this is new content"
}
get_response=requests.put(endpoints,json=data)



print(get_response.json())
print(get_response.status_code)