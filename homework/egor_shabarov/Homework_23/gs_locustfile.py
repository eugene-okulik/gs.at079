from locust import task, HttpUser
import random

class ObjectUser(HttpUser):
    id_obj = None

    def on_start(self):
        """Создаем один объект для пользователя"""
        body = {"name": "test_obj", "data": {"color": "white", "size": "big"}}
        response = self.client.post(f'/object', json=body)
        self.id_obj = response.json()['id']
        print(f"Пользователь создал объект: {self.id_obj}")

    def on_stop(self):
        """Удаляем объект после завершения"""
        self.client.delete(f'/object/{self.id_obj}')

    @task(3)
    def test_get_one_object(self):
        self.client.get(f'/object/{self.id_obj}', name='GET /object/{id}')  # Добавил name, чтобы отличать два вида get запроса

    @task(1)
    def test_get_all_object(self):
        self.client.get('/object')

    @task(2)
    def test_put_object(self):
        body = {'name': f'name_{random.randrange(1, 10000)}', 'data': {'color': 'new_color', 'size': 'new_size'}}
        self.client.put(f'/object/{self.id_obj}', json=body, name='PUT /object/{id}')

    @task(2)
    def test_patch_name_object(self):
        body = {'name': f'patched_name_{random.randrange(1, 10000)}'}
        self.client.patch(f'/object/{self.id_obj}', json=body, name='PATCH /object/{id} (name)')

    @task(1)
    def test_create_object(self):
        body = {"name": f"test_{random.randrange(1, 10000)}", "data": {"color": "white", "size": "big"}}
        response = self.client.post('/object', json=body, name='POST /object')
        temp_id = response.json()['id']
        self.client.delete(f'/object/{temp_id}', name='DELETE /object/{id}')







# BASE_URL = 'http://objapi.course.qa-practice.com'
#
#
# @pytest.fixture(scope='session')
# def print_text_session():
#     print("Start testing")
#     yield
#     print("Testing completed")
#
#
# @pytest.fixture()
# def print_text_func():
#     print('before test')
#     yield
#     print('\nafter test')
#
#
# @pytest.fixture
# def create_obj():
#     body = {"name": "test_obj", "data": {"color": "white", "size": "big"}}
#     response = requests.post(f'{BASE_URL}/object', json=body)
#     id_obj = response.json()['id']
#     yield id_obj
#     requests.delete(f'{BASE_URL}/object/{id_obj}')
#
#
# @pytest.mark.medium
# def test_get_all_object(print_text_session, print_text_func):
#     response = requests.get(f'{BASE_URL}/object')
#     assert response.status_code == 200
#
#
# def test_get_one_object(create_obj, print_text_func):
#     response = requests.get(f'{BASE_URL}/object/{create_obj}')
#     assert response.status_code == 200
#     assert response.json()['name'] == 'test_obj'
#
#
# @pytest.mark.critical
# def test_post_object():
#     body = {
#         'name': 'name_one',
#         'data': {
#             'color': 'red',
#             'size': 'big'
#         }
#     }
#     response = requests.post(f'{BASE_URL}/object', json=body)
#     print(response.json()['id'])
#     assert response.status_code == 200
#     assert response.json()['name'] == 'name_one'
#
#
# @pytest.mark.parametrize('new_name, new_color, new_size', [('new_name', 'new_color', 'new_size')])
# def test_put_object(print_text_func, create_obj, new_name, new_color, new_size):
#     body = {
#         'name': new_name,
#         'data': {
#             'color': new_color,
#             'size': new_size
#         }
#     }
#     response = requests.put(f'{BASE_URL}/object/{create_obj}', json=body)
#     assert response.status_code == 200
#     assert response.json()['name'] == new_name
#
#
# @pytest.mark.parametrize('new_name', ['new name'])
# def test_patch_name_obj(print_text_func, create_obj, new_name):
#     body = {'name': new_name}
#     response = requests.patch(f'{BASE_URL}/object/{create_obj}', json=body)
#     assert response.status_code == 200
#     assert response.json()['name'] == new_name
#
#
# def test_patch_color_obj(print_text_func, create_obj):
#     new_color = 'new_color'
#     body = {'data': {'color': new_color}}
#     response = requests.patch(f'{BASE_URL}/object/{create_obj}', json=body)
#     assert response.status_code == 200
#     assert response.json()['data']['color'] == new_color
#
#
# def test_delete_obj(print_text_func, create_obj):
#     response = requests.delete(f'{BASE_URL}/object/{create_obj}')
#     assert response.status_code == 200
#     assert response.text == f'Object with id {create_obj} successfully deleted'
