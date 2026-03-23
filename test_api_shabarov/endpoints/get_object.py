import requests
import allure

from test_api_shabarov.endpoints.base_endpoint import BaseEndpoint


class GetObject(BaseEndpoint):
    @allure.step('Отправка GET запроса для получения всех объектов')
    def get_all_object(self):
        self.response = requests.get(f'{self.BASE_URL}/object')
        return self.response

    @allure.step('Отправка GET запроса для получения одного объекта')
    def get_one_object(self, obj_id):
        self.response = requests.get(f'{self.BASE_URL}/object/{obj_id}')
        return self.response
