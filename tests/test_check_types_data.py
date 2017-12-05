import requests


# def test_check_types_data():
#     r = requests.get('http://127.0.0.1:5000/todo/api/v1.0/tasks')
#     for i in r.json()['tasks']:
#          assert type(i['description']) == str
#          assert type(i['done']) == bool
#          assert type(i['id']) == int
#          assert type(i['title']) == str


def test_check_types_data():
    r = requests.get('http://127.0.0.1:5000/todo/api/v1.0/tasks')
    for i in range(len(r.json()['tasks'])):
        assert type(r.json()['tasks'][i]['description']) == str
        assert type(r.json()['tasks'][i]['done']) == bool
        assert type(r.json()['tasks'][i]['id']) == int
        assert type(r.json()['tasks'][i]['title']) == str




