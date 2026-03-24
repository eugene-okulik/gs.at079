import requests
import allure

from test_api_shabarov.endpoints.base_endpoint import BaseEndpoint


class CreateObject(BaseEndpoint):
    id_object = None

    @allure.step('Отправка POST запроса для создания объекта')
    def create_new_object(self, body):
        self.response = requests.post(f'{self.BASE_URL}/object', json=body)
        self.json_response = self.response.json()
        self.id_object = self.json_response['id']
        return self.response
