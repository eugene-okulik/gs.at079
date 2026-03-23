import requests
import allure

from test_api_shabarov.endpoints.base_endpoint import BaseEndpoint


class PutObject(BaseEndpoint):

    @allure.step('Отправка PUT запроса для полного изменения объекта')
    def full_change_object(self, id_obj, body):
        self.response = requests.put(f'{self.BASE_URL}/object/{id_obj}', json=body)
        return self.response
