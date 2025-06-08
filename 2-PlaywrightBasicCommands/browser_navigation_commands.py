import time

from playwright.sync_api import Page

def test_navigate_browser(page):
    page.goto('https:facebook.com')
    title=page.title()
    print(title)
    assert 'Facebook – log in or sign up' in title

    page.goto('https://gmail.com')
    time.sleep(5.0)
    title=page.title()
    print(title)

    print('+++++++++++++++++++++')
    page.wait_for_timeout(2000)
    page.go_back()
    page.wait_for_timeout(2000)
    page.go_forward()
    page.wait_for_timeout(2000)
    page.reload()
