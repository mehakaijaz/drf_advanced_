import requests

endpoints='http://127.0.0.1:8000/api/products/'



data={'title': 'This field is done.', 'content': 'This field is done.'}

get_response=requests.post(endpoints,json=data)
print(get_response.json())
print(get_response.status_code)