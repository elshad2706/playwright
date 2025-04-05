import re
import time
from playwright.sync_api import Page, Route, expect
import playwright
from playwright.async_api import Page
from playwright.sync_api import Playwright, sync_playwright, expect
from pathlib import Path


def test_listen_network(page: Page):
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    page.goto('https://osinit.ru/')


def test_network(page):
    page.route("**/register", lambda route: route.continue_(post_data='{"email": "user","password": "secret"}'))
    page.goto('https://reqres.in/')
    page.get_by_text(' Register - successful ').click()


def test_intercepted(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        json = response.json()
        json['data']['country'] = 'Azer'
        json['data']['city'] = 'Mariel'
        json['data']['zip_code'] = 423339
        json['data']['latitude'] = 45.7524
        json['data']['ip_address'] = '177.277.77.177'
        route.fulfill(json=json)

    page.route("**/api/tools/get-ip-address-information", handle_route)
    page.goto("https://belurk.ru/services/my-ip")


def test_replace_from_har(page):
    page.goto("https://reqres.in/")
    page.route_from_har("example.har")
    users_single = page.locator('li[data-id="users-single"]')
    users_single.click()
    response = page.locator('[data-key="output-response"]')
    expect(response).to_contain_text("Open solution")



