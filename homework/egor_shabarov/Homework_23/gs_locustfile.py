from locust import task, HttpUser
import random


class ObjectUser(HttpUser):
    id_obj = None

    def on_start(self):
        """Создаем один объект для пользователя"""
        body = {"name": "test_obj", "data": {"color": "white", "size": "big"}}
        response = self.client.post('/object', json=body)
        self.id_obj = response.json()['id']
        print(f"Пользователь создал объект: {self.id_obj}")

    def on_stop(self):
        """Удаляем объект после завершения"""
        self.client.delete(f'/object/{self.id_obj}')

    @task(3)
    def test_get_one_object(self):
        self.client.get(f'/object/{self.id_obj}', name='GET /object/{id}')  # Добавил name, чтобы отличать два get gi

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
