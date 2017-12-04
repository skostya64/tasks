import requests


r = requests.get('http://127.0.0.1:5000/todo/api/v1.0/tasks')


def test_check_type_data_description():
    print(type(r.json()['tasks'][0]['description']))
    assert type(r.json()['tasks'][0]['description']) == str