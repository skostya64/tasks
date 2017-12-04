import requests


r = requests.get('http://127.0.0.1:5000/todo/api/v1.0/tasks')

print(type(r.status_code))
print(type(r.json()['tasks'][0]['description']))
print(type(r.json()['tasks'][0]['done']))
print(type(r.json()['tasks'][0]['id']))
print(type(r.json()['tasks'][0]['title']))