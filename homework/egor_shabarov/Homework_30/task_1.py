import json

from playwright.sync_api import Page, expect, Route

import re
from time import sleep


def test_one(page: Page):

    new_name_prod = 'Яблокофон 17 про'

    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = new_name_prod
        body["body"]["digitalMat"][0]["familyTypes"][0]["tabTitle"] = new_name_prod
        body = json.dumps(body)

        route.fulfill(response=response, body=body)

    page.route(re.compile('api/digital-mat'), handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')

    page.get_by_role('heading', name='iPhone 17 Pro & iPhone 17 Pro Max').click()

    # heading = page.locator('#rf-digitalmat-overlay-label-0').nth(0)
    heading = page.get_by_role('heading', name=new_name_prod, exact=True)

    expect(heading).to_be_visible()
    expect(heading).to_have_text(new_name_prod)
    sleep(5)
