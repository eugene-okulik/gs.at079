from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import string


options = Options()
options.add_argument('start-maximized')
driver: WebDriver = webdriver.Chrome(options=options)

driver.get('https://www.qa-practice.com/elements/input/simple')

text_string = driver.find_element(By.CSS_SELECTOR, '[placeholder="Submit me"]')
text_input = ''.join(random.choices(string.ascii_lowercase, k=10))
text_string.send_keys(text_input)
# text_string.send_keys(Keys.ENTER)
text_string.submit()

result = driver.find_element(By.XPATH, '//*[@id="result-text"]')

print(f'\n {result.text}')
assert result.text == text_input
