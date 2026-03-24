import requests
import allure

from test_api_shabarov.endpoints.base_endpoint import BaseEndpoint


class PatchObject(BaseEndpoint):

    @allure.step('Отправка PATCH запроса для частичного изменения объекта')
    def patch_object(self, id_obj, body):
        self.response = requests.patch(f'{self.BASE_URL}/object/{id_obj}', json=body)
        return self.response
