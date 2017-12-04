import requests


r = requests.get('http://127.0.0.1:5000/todo/api/v1.0/tasks')

print(r.status_code)
print(r.json()['tasks'][0]['description'])
print(r.json()['tasks'][0]['done'])
print(r.json()['tasks'][0]['id'])
print(r.json()['tasks'][0]['title'])