import requests

GIT_URL = 'https://api.github.com/events'

r_get = requests.get(GIT_URL)
# r is a response objec, we can get all the information from this object

# Requests simple api means that all forms of HTTP request are as obvious.
# for ex. we can make an HTTP POST request:
r_post = requests.post(GIT_URL+"/post", data = {'key': 'value'})

r_put = requests.put('https://httpbin.org/put', data={'key': 'value'})
r_del = requests.delete('https://httpbin.org/delete')
r_head = requests.head('https://httpbin.org/get')
r_opt = requests.options('https://httpbin.org/get')


## Passing parameters in URLs
# Requests allows us to provide the arguments as a dictionary of strings, using the params keyword argument. 
payload = {'key1': 'value1', 'key2': 'value2'}
parametere_passing = requests.get('https://httpbin.org/get', params=payload)

print(parametere_passing.url)
# https://httpbin.org/get?key2=value2&key1=value1

# any dictionary key whose value is None will not be added to the URL’s query string. We can also pass a list of items as a value:

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
parameter_list = requests.get('https://httpbin.org/get', params=payload)
print(parameter_list.url)
# https://httpbin.org/get?key1=value1&key2=value2&key2=value3



# Response Content

# We can read the content of the server’s response. Consider the GitHub timeline again:
r_get.text
# '[{"repository":{"open_issues":0,"url":"https://github.com/...

#  can also access the response body as bytes, for non-text requests:
r_get.content
# b'[{"repository":{"open_issues":0,"url":"https://github.com/...


# JSON Response Content
# There’s also a builtin JSON decoder, in case you’re dealing with JSON data:

r = requests.get('https://api.github.com/events')
print(r.json())

# [{'repository': {'open_issues': 0, 'url': 'https://github.com/...

# exampro.co/terraform