import pytest
import allure


create_data = [
    {'name': 'name 1', 'data': {'color': 'red', 'size': 'big'}},
    {'name': 'name 2', 'data': {'color': 'red', 'size': 'big'}},
    {'name': 'name 3', 'data': {'color': 'red', 'size': 'big'}}
]

put_data = [('new_name', 'new_color', 'new_size')]


@allure.title('Получение всех объектов')
def test_get_all_objects(get_object_endpoint):
    get_object_endpoint.get_all_object()
    get_object_endpoint.check_status_200()


@allure.title('Получение одного объекта')
def test_get_one_object(get_object_endpoint, create_obj_id):
    get_object_endpoint.get_one_object(create_obj_id)
    get_object_endpoint.check_status_200()
    get_object_endpoint.check_response_id_is_correct(create_obj_id)


@allure.title('Создание объекта')
@pytest.mark.parametrize('body', create_data)
def test_post_object(create_object_endpoint, body):
    create_object_endpoint.create_new_object(body)
    create_object_endpoint.check_status_200()
    create_object_endpoint.check_response_name_is_correct(body['name'])


@allure.title('Полное изменение объекта')
def test_put_object(put_object_endpoint, create_obj_id):
    body = {'name': 'new_name', 'data': {'color': 'new_color', 'size': 'new_size'}}
    put_object_endpoint.full_change_object(create_obj_id, body)
    put_object_endpoint.check_status_200()
    put_object_endpoint.check_response_name_is_correct(body['name'])


@allure.title('Изменение имени объекта')
def test_patch_name_obj(patch_object_endpoint, create_obj_id):
    body = {'name': 'new_name'}
    patch_object_endpoint.patch_object(create_obj_id, body)
    patch_object_endpoint.check_status_200()
    patch_object_endpoint.check_response_name_is_correct(body['name'])


@allure.title('Удаление объекта')
def test_delete_obj(delete_object_endpoint, create_obj_id):
    delete_object_endpoint.delete_object(create_obj_id)
    delete_object_endpoint.check_status_200()
    delete_object_endpoint.check_text_after_del(create_obj_id)
