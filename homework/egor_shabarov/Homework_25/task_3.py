import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('start-maximized')
    driver : WebDriver = webdriver.Chrome(options=options)
    yield driver


def test_3_part_1(driver):

    driver.get('https://www.qa-practice.com/elements/select/single_select')
    selecte_language = Select(driver.find_element(By.XPATH, '//*[@id="id_choose_language"]'))
    selecte_language.select_by_visible_text('Python')

    driver.find_element(By.XPATH, '//*[@id="submit-id-submit"]').click()

    wait = WebDriverWait(driver, 10)
    result_text = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="result-text"]'))).text
    assert result_text == 'Python'


def test_3_part_2(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')

    driver.find_element(By.XPATH, "//div[@id='start']/button[text()='Start']").click()

    wait = WebDriverWait(driver, 10)
    finish_text = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                              "//*[@id='finish']/h4[text()='Hello World!']")))
    assert finish_text.text == "Hello World!"
