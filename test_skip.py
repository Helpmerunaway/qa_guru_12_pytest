import pytest
from selene import by, be
from selene.support.shared import browser

url = 'https://github.com'

chrome = pytest.fixture(params=[(1600, 900), (1280, 1024), (414, 896), (320, 768)])


@chrome
def browser_size(request):
    return request


@pytest.fixture(scope='function', autouse=True)
def set_up_browser(browser_size):
    width = browser_size.param[0]
    height = browser_size.param[1]

    browser.config.window_width = width
    browser.config.window_height = height

    browser.open(url)


def test_github_desktop():
    if browser._config.window_width < 1200:
        pytest.skip('Wrong Size. Not for desktop')
    browser.element('a[href="/login').click()
    browser.element(by.partial_text("Sign in")).should(be.visible)


def test_github_mobile():
    if browser._config.window_width > 1000:
        pytest.skip(f'Wrong Size. Not for mobile')
    browser.element('[class="octicon octicon-three-bars"]').click()
    browser.element('a[href="/login').click()
    browser.element(by.partial_text("Sign in")).should(be.visible)
