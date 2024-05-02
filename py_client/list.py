import requests
from getpass import getpass

endpoint='http://127.0.0.1:8000/api/auth/'
username=input("What is your username?\n")
password=getpass("What is your password?\n")

auth_response=requests.post(endpoint,json={'username': username, 'password':password})
print(auth_response.json())
if auth_response.status_code==200:
    token=auth_response.json()['token']
    headers={
        'Authorization':f'Bearer {token}'
    }
    endpoints='http://127.0.0.1:8000/api/products/'

    #data={'title': 'This field is done.', 'content': 'This field is done.'}

    get_response=requests.get(endpoints,headers=headers)
    print(get_response.json())
    print(get_response.status_code)