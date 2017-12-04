import requests


r = requests.get('http://127.0.0.1:5000/todo/api/v1.0/tasks')


def test_check_types_data():
    r = requests.get('http://127.0.0.1:5000/todo/api/v1.0/tasks')
    assert type(r.json()['tasks'][0]['description']) == str
    assert type(r.json()['tasks'][0]['done']) == bool
    assert type(r.json()['tasks'][0]['id']) == int
    assert type(r.json()['tasks'][0]['title']) == str