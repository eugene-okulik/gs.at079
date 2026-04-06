import pytest
from selenium import webdriver

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException


URL = 'http://testshop.qa-practice.com/'


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    driver: WebDriver = webdriver.Chrome(options=options)
    yield driver


def test_add_to_cart_new_tabs(driver):

    wait = WebDriverWait(driver, 5)

    driver.get(URL)

    product_table = driver.find_element(By.XPATH, '//*[@content="Customizable Desk"]')

    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).click(product_table).key_up(Keys.CONTROL).perform()

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    driver.find_element(By.ID, 'add_to_cart').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Continue Shopping"]'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(@class, "my_cart_quantity") and text()="1"]')))

    driver.close()
    driver.switch_to.window(tabs[0])

    try:
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[contains(@class, "my_cart_quantity") and text()="1"]'))).click()
    except TimeoutException:
        driver.refresh()

    driver.find_element(By.CLASS_NAME, 'o_wsale_my_cart').click()

    try:
        product_cart = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "align-top")))
    except TimeoutException:
        driver.refresh()
        product_cart = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "align-top")))

    print(product_cart.text)
    assert product_cart.text == 'Customizable Desk (Steel, White)'


def test_add_to_cart_hover(driver):

    product_name = 'Customizable Desk'

    wait = WebDriverWait(driver, 5)
    action = ActionChains(driver)

    driver.get(URL)

    product_table = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//img[@alt="Customizable Desk"]')))

    action.move_to_element(product_table).perform()

    cart_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="Shopping cart"]')))
    cart_btn.click()

    modal_window = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content')))
    modal_window_text = modal_window.find_element(By.CLASS_NAME, 'modal-title').text
    assert modal_window_text == 'Add to cart', 'Панель корзины не открылась'

    table_in_cart = driver.find_element(
        By.XPATH, '//*[contains(@class, "in_cart")]//*[contains(@class, "product-name")]')
    assert product_name in table_in_cart.text, f' Товара {product_name} нет в корзине'
