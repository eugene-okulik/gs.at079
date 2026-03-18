import pytest
import allure


@pytest.fixture()
def setup():
    pass


@allure.feature('ficha_1')
@allure.story('story_1')
@allure.title('Тест функциональности №1')
@allure.severity(allure.severity_level.CRITICAL)
def test_1_1():
    assert 1 == 1


@allure.feature('ficha_1')
@allure.story('story_1')
@allure.title('Тест функциональности №2')
@allure.severity(allure.severity_level.CRITICAL)
def test_2_1():
    with allure.step('Шаг 1: Подготовка тестовых данных'):
        a = 23423
        a += 1
    with allure.step('Шаг 2 Проверка ответа'):
        assert 2 == 5


@allure.feature('ficha_1')
@allure.story('story_2')
def test_3_1():
    assert 3 == 3


@allure.feature('ficha_2')
@allure.story('story_2')
def test_4_1():
    assert 4 == 4


@allure.feature('ficha_2')
def test_1_2():
    assert 1 == 1


@allure.feature('ficha_2')
@allure.story('story_1')
def test_2_2():
    assert 2 == 3


@allure.feature('ficha_2')
@allure.story('story_2')
def test_3_2():
    assert 3 == 2


@allure.feature('ficha_2')
@allure.story('story_2')
def test_4_2():
    assert 3 == 3
