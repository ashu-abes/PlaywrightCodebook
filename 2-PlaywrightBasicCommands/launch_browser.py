from playwright.sync_api import Page

def test_first_example(page):
    page.goto('http://google.com')
    title=page.title()
    print(title)
    assert 'Google' in title
    page.wait_for_timeout(20000)