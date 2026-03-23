import requests
import allure

from test_api_shabarov.endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):

    @allure.step('Отправка DELETE запроса')
    def delete_object(self, id_obj):
        self.response = requests.delete(f'{self.BASE_URL}/object/{id_obj}')
        return self.response

    @allure.step('Проверяем соответствия текста в ответе после удаления')
    def check_text_after_del(self, id_obj):
        assert self.response.text == f'Object with id {id_obj} successfully deleted'
