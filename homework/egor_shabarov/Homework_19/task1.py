import requests

BASE_URL = 'http://objapi.course.qa-practice.com'


def get_all_object():
    response = requests.get(f'{BASE_URL}/object')
    print(response.status_code)
    print(len(response.json()['data']))
    assert response.status_code == 200


def get_one_object(id):
    response = requests.get(f'{BASE_URL}/object/{id}')
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200
    assert response.json()['name'] == 'First object'


def post_object(name):
    body = {
        'name': name,
        'data': {
            'color': 'red',
            'size': 'big'
        }
    }
    response = requests.post(f'{BASE_URL}/object', json=body)
    print(response.status_code)
    print(response.json()['id'])
    assert response.status_code == 200
    assert response.json()['name'] == name


def put_object(id, new_name, new_color, new_size):
    body = {
        'name': new_name,
        'data': {
            'color': new_color,
            'size': new_size
        }
    }
    response = requests.put(f'{BASE_URL}/object/{id}', json=body)
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200
    assert response.json()['name'] == new_name


def patch_name_obj(id, new_name):
    body = {'name': new_name}
    response = requests.patch(f'{BASE_URL}/object/{id}', json=body)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['name'] == new_name


def patch_color_obj(id, new_color):
    body = {'data': {'color': new_color}}
    response = requests.patch(f'{BASE_URL}/object/{id}', json=body)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['data']['color'] == new_color


def delete_obj(id):
    response = requests.delete(f'{BASE_URL}/object/{id}')
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200
    assert response.text == f'Object with id {id} successfully deleted'


# get_all_object()
# get_one_object(1)
# post_object('gs object 2')
# put_object(5116, 'new gs obj', 'green', 'small')
# patch_name_obj(5116, 'new gs obj-2')
# patch_color_obj(5116, 'new color-2')
# delete_obj(5116)
