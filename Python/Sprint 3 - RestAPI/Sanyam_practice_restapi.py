import requests, json

BASE_URL="http://jsonplaceholder.typicode.com/todos"

POST_DATA = {"userId":1,"title":"foO","completed":False}
print(type(POST_DATA))
response = requests.post(BASE_URL , json=POST_DATA)
print(response, response.json(), response.headers["content-type"])


POST_DATA_1 = {"userId":1,"title":"foO","completed":False}
print(type(POST_DATA_1))
my_headers = {'content-type':'application/json'}
response = requests.post(BASE_URL,data=json.dumps(POST_DATA_1),headers=my_headers)
print(response , response.json() , response.headers)


BASE_URL_1 = "http://jsonplaceholder.typicode.com/todos/10"
response = requests.get(BASE_URL_1 )
print(response, response.json())

PUT_DATA = {"userId":3,"title":"bar","completed":False}
response = requests.put(BASE_URL_1 , json=PUT_DATA)
print(response.json())

PATCH_DATA = {"Title":"Python Programing"}
response = requests.patch(BASE_URL_1 ,PATCH_DATA)
print(response.json(), response)


PATCH_DATA_1 = {"userId":3,"title":"python","completed":False}
response = requests.patch(BASE_URL_1 , PATCH_DATA_1)
print(response.json(), response)


PUT_DATA = {"userId":3,"completed":False}
response = requests.put(BASE_URL_1, PUT_DATA)

response = requests.delete(BASE_URL_1)
print(response.json)





'''
OUTPUT -------------------------------

<class 'dict'>
<Response [201]> {'userId': 1, 'title': 'foO', 'completed': False, 'id': 201} application/json; charset=utf-8
<class 'dict'>
<Response [201]> {'userId': 1, 'title': 'foO', 'completed': False, 'id': 201} {'Date': 'Fri, 10 Feb 2023 15:22:51 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '70', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'X-Ratelimit-Limit': '1000', 'X-Ratelimit-Remaining': '998', 'X-Ratelimit-Reset': '1676042583', 'Vary': 'Origin, X-HTTP-Method-Override, Accept-Encoding', 'Access-Control-Allow-Credentials': 'true', 'Cache-Control': 'no-cache', 'Pragma': 'no-cache', 'Expires': '-1', 'Access-Control-Expose-Headers': 'Location', 'Location': 'http://jsonplaceholder.typicode.com/todos/201', 'X-Content-Type-Options': 'nosniff', 'Etag': 'W/"46-Qqn1TNMZK86MXXeAYK/FOW+jYRc"', 'Via': '1.1 vegur', 'CF-Cache-Status': 'DYNAMIC', 'Server-Timing': 'cf-q-config;dur=7.9999999798019e-06', 'Report-To': '{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=T%2FTWLqHzFdu%2BP6rN7giJOQkzmMmkXYzm6jb4MccGWCjBKY%2B%2BVGoJUauvRWQlgotqok3FrpEeagX4t82ksERnBeiHHyOO%2FVsiA4TxA64D4XwbAKDFnj2FDY9KRjyVIXm1eb8ANwzM5NMGZn8xVF0yHfVr762wqa60OGXD"}],"group":"cf-nel","max_age":604800}', 'NEL': '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}', 'Server': 'cloudflare', 'CF-RAY': '7975d7b488a1f4b0-BOM', 'alt-svc': 'h3=":443"; ma=86400, h3-29=":443"; ma=86400'}
<Response [200]> {'userId': 1, 'id': 10, 'title': 'illo est ratione doloremque quia maiores aut', 'completed': True}
{'userId': 3, 'title': 'bar', 'completed': False, 'id': 10}
{'userId': 1, 'id': 10, 'title': 'illo est ratione doloremque quia maiores aut', 'completed': True, 'Title': 'Python Programing'} <Response [200]>
{'userId': '3', 'id': 10, 'title': 'python', 'completed': 'False'} <Response [200]>
<bound method Response.json of <Response [200]>>

'''