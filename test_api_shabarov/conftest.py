import pytest

from test_api_shabarov.endpoints.create_obj import CreateObject
from test_api_shabarov.endpoints.get_object import GetObject
from test_api_shabarov.endpoints.put_object import PutObject
from test_api_shabarov.endpoints.patch_object import PatchObject
from test_api_shabarov.endpoints.delete_object import DeleteObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def put_object_endpoint():
    return PutObject()


@pytest.fixture()
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def create_obj_id(create_object_endpoint, delete_object_endpoint):
    body = {"name": "test_obj", "data": {"color": "white", "size": "big"}}
    create_object_endpoint.create_new_object(body)
    id_object = create_object_endpoint.id_object
    yield id_object
    delete_object_endpoint.delete_object(id_object)
