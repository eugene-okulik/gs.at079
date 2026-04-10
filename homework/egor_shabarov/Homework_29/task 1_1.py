from playwright.sync_api import Page, expect, Dialog, BrowserContext


def test_allert(page: Page):

    def accept_allert(alert: Dialog):
        alert.accept()

    page.goto('https://www.qa-practice.com/elements/alert/confirm')

    page.on('dialog', accept_allert)
    # page.on('dialog', lambda alert: alert.accept())
    page.get_by_role('link', name='Click').click()

    expect(page.locator('.result-text')).to_have_text('Ok')

    # result_text = page.locator('.result')
    # expect(result_text).to_contain_text('You selected')
    # expect(result_text).to_contain_text('Ok')


def test_new_page(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')

    with context.expect_page() as new_page_event:
        page.get_by_role('link', name='Click').click()
    new_page = new_page_event.value

    expect(new_page.locator('.result-text')).to_have_text('I am a new page in a new tab')
    new_page.close()

    expect(page.get_by_role('link', name='Click')).to_be_enabled()


def test_color_change(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')

    color_btn = page.get_by_role('button', name='Color Change')
    expect(color_btn).to_have_css('color', 'rgb(220, 53, 69)', timeout=10000)
    color_btn.click()
