from playwright.sync_api import Page, expect


def test_invalid_login(page: Page):
    login = 'test_user3423'
    passw = 'sadasd2134F'

    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='Username').fill(f'{login}')
    page.get_by_role('textbox', name='Password').fill(f'{passw}')
    page.get_by_role('button', name='Login').click()
    text_username_invalid = page.get_by_text('Your username is invalid!')
    expect(text_username_invalid).to_be_visible()


def test_fill_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_role('textbox', name='First Name').fill('Anton')
    page.get_by_placeholder('Last Name').fill('Makov')
    page.get_by_role('textbox', name='name@example.com').fill('testmail@yandex.com')
    page.get_by_text('Female').click()
    page.get_by_role('textbox', name='Mobile Number').fill('9808898909')
    date_of_bird = page.locator('//*[@id="dateOfBirthInput"]')
    date_of_bird.click()
    date_of_bird.press('Enter+a')
    date_of_bird.press('Backspace')
    date_of_bird.fill('09 Apr 2026')
    subjects = page.locator('.subjects-auto-complete__input')
    subjects.fill('Arts')
    subjects.press('Enter')
    page.get_by_role('checkbox', name='Sports').click()
    page.get_by_role('textbox', name='Current Address').fill('test adress')
    state = page.locator('#react-select-3-input')
    state.fill('NCR')
    state.press('Enter')
    city = page.locator('#react-select-4-input')
    city.fill('Delhi')
    city.press('Enter')
    page.get_by_role('button', name='Submit').click()
    expect(page.get_by_text('Thanks for submitting the form')).to_be_visible()
