from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
from time import sleep


options = Options()
options.add_argument('start-maximized')
driver: WebDriver = webdriver.Chrome(options=options)

driver.get('https://demoqa.com/automation-practice-form')
assert driver.title == 'demosite'

first_name_string = driver.find_element(By.XPATH, '//*[@placeholder="First Name"]')
first_name_string.send_keys('Иван')

last_name_string = driver.find_element(By.XPATH, '//*[@id="lastName"]')
last_name_string.send_keys('Петров')

mail = driver.find_element(By.XPATH, '//*[@id="userEmail"]')
mail.send_keys('test_4124@mail.ru')

radio_male = driver.find_element(By.XPATH, '//*[@type="radio" and @value="Male"]')
radio_male.click()
assert radio_male.is_selected(), "Радиокнопка 'Male' не выбрана"

mobile_string = driver.find_element(By.XPATH, '//*[@placeholder="Mobile Number"]')
mobile_number = ''.join(random.choices(string.digits, k=10))
mobile_string.send_keys(mobile_number)

date = driver.find_element(By.XPATH, '//*[@id="dateOfBirthInput"]')
# Первый вариант с датой
# date.click()
# date.clear()
# date.send_keys('03 May 2010')
# date.send_keys(Keys.ENTER)

# Второй вараинт с датой
date.click()

year = driver.find_element(By.XPATH, '//*[@class="react-datepicker__year-select"]')
select_year = Select(year)
select_year.select_by_value('2010')

month = driver.find_element(By.XPATH, '//*[@class="react-datepicker__month-select"]')
select_month = Select(month)
select_month.select_by_visible_text('May')

day = driver.find_element(By.XPATH, '//*[@aria-label="Choose Saturday, May 15th, 2010"]')
day.click()

subject_auto_complete = driver.find_element(By.XPATH, '//*[@id="subjectsInput"]')
subject_auto_complete.send_keys('math')
subject_auto_complete.send_keys(Keys.ENTER)

hobbies_music_chekbox = driver.find_element(By.XPATH, '//label[@class="form-check-label" and text()="Music"]')
hobbies_music_chekbox.click()

address_textarea = driver.find_element(By.XPATH, '//*[@placeholder="Current Address"]')
address_textarea.send_keys('Москва, ул. Ленина, д. 23')

state = driver.find_element(By.XPATH, '//*[@id="react-select-3-input"]')
state.send_keys('Haryana')
state.send_keys(Keys.ENTER)
sleep(3)

city = driver.find_element(By.XPATH, '//*[@id="react-select-4-input"]')
city.send_keys('Karnal')
city.send_keys(Keys.ENTER)

submit_btn = driver.find_element(By.XPATH, '//*[@id="submit"]')
submit_btn.click()

table_data = driver.find_element(By.XPATH,
                                 '//*[@class="table-responsive"]')
print(table_data.get_attribute("innerText"))

# Второй вариант (и так для каждой строки)
# wait = WebDriverWait(driver, 10)
# student_name = wait.until(EC.visibility_of_element_located((By.XPATH,
#                                                             "//td[text()='Student Name']/following-sibling::td")))
# print(f"Student Name: {student_name.text}")
