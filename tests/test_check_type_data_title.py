import requests


r = requests.get('http://127.0.0.1:5000/todo/api/v1.0/tasks')


def test_check_type_data_title():
    print(type(r.json()['tasks'][0]['title']))
    assert type(r.json()['tasks'][0]['title']) == str