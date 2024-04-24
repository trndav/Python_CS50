import requests
url="https://ibm.com/"
r = requests.get(url)
print(r.status_code)
print(r)
print("Headers: ", r.headers)
print("Body: ", r.request.body) # No body for GET request here
print("Last modified: ", r.headers["Last-Modified"])

print("First 50 chars:", r.text[0:50])

url_get = 'http://httpbin.org/get'
payload = {"name":"Joseph","ID":"123"}
r = requests.get(url_get,params=payload)
print(r.url)
print("Body: ", r.request.body) # No body for GET request here
print("First 50 chars:", r.text[0:50])
print("Headers ", r.headers['Content-Type'])


url_post = 'http://httpbin.org/post'
payload = {"name":"Joseph","ID":"123"}
r_post = requests.post(url_post,data=payload)
print("post url:", r_post.url)
print("get url:", r.url)
