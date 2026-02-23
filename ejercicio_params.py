import requests
url = "https://dummyjson.com/products"

params = {"limit":3}
response = requests.get(url, params=params)

print (response.url)
print (response.json())