import pytest
import requests

BASE_URL = 'http://objapi.course.qa-practice.com'


@pytest.fixture(scope='session')
def print_text_session():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture()
def print_text_func():
    print('before test')
    yield
    print('\nafter test')


@pytest.fixture
def create_obj():
    body = {"name": "test_obj", "data": {"color": "white", "size": "big"}}
    response = requests.post(f'{BASE_URL}/object', json=body)
    id_obj = response.json()['id']
    yield id_obj
    requests.delete(f'{BASE_URL}/object/{id_obj}')


@pytest.mark.medium
def test_get_all_object(print_text_session, print_text_func):
    response = requests.get(f'{BASE_URL}/object')
    assert response.status_code == 200


def test_get_one_object(create_obj, print_text_func):
    response = requests.get(f'{BASE_URL}/object/{create_obj}')
    assert response.status_code == 200
    assert response.json()['name'] == 'test_obj'


@pytest.mark.critical
@pytest.mark.parametrize('name', ['name_one', 'name_two', 'name_lalala'])
def test_post_object(print_text_func, name):
    body = {
        'name': name,
        'data': {
            'color': 'red',
            'size': 'big'
        }
    }
    response = requests.post(f'{BASE_URL}/object', json=body)
    assert response.status_code == 200
    assert response.json()['name'] == name


@pytest.mark.parametrize('new_name, new_color, new_size', [('new_name', 'new_color', 'new_size')])
def test_put_object(print_text_func, create_obj, new_name, new_color, new_size):
    body = {
        'name': new_name,
        'data': {
            'color': new_color,
            'size': new_size
        }
    }
    response = requests.put(f'{BASE_URL}/object/{create_obj}', json=body)
    assert response.status_code == 200
    assert response.json()['name'] == new_name


@pytest.mark.parametrize('new_name', ['new name'])
def test_patch_name_obj(print_text_func, create_obj, new_name):
    body = {'name': new_name}
    response = requests.patch(f'{BASE_URL}/object/{create_obj}', json=body)
    assert response.status_code == 200
    assert response.json()['name'] == new_name


def test_patch_color_obj(print_text_func, create_obj):
    new_color = 'new_color'
    body = {'data': {'color': new_color}}
    response = requests.patch(f'{BASE_URL}/object/{create_obj}', json=body)
    assert response.status_code == 200
    assert response.json()['data']['color'] == new_color


def test_delete_obj(print_text_func, create_obj):
    response = requests.delete(f'{BASE_URL}/object/{create_obj}')
    assert response.status_code == 200
    assert response.text == f'Object with id {create_obj} successfully deleted'
