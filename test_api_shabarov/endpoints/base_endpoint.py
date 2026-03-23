import allure


class BaseEndpoint:
    BASE_URL = 'http://objapi.course.qa-practice.com'
    response = None
    json_response = None

    @allure.step('Проверка, что статус код в ответе 200')
    def check_status_200(self):
        assert self.response.status_code == 200

    @allure.step('Проверка, что имя объекта соответствует переданному имени')
    def check_response_name_is_correct(self, name):
        assert self.response.json()['name'] == name
