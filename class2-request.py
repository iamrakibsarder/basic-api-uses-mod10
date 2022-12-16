import requests

res = requests.get('https://jsonplaceholder.typicode.com/users')
print(res.json())
print(res.status_code)