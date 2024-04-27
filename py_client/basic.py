import requests

#endpoints='https://httpbin.org/status/200/'
#endpoints='https://httpbin.org/'
endpoints='http://127.0.0.1:8000/' #'http://localhost:8000/'
#requests.get() #application programming interface
get_response=requests.get(endpoints) #http request
print(get_response.text) #print the source code of the api
#phone=camera=app=api=camera(library apis)
#rest apis=web api

#http request=html
#REST API STILL HTTP REQUEST= JSON(XML)
#json~python dict
#print(get_response.json())
print(get_response.status_code)