import pytest
from selene import by, be
from selene.support.shared import browser

url = 'https://github.com'

chrome = pytest.fixture(params=[(1600, 900), (1280, 1024), (414, 896), (320, 768)])


@chrome
def browser_size(request):
    return request


@pytest.fixture(scope='function', autouse=True)
def browser_settings(browser_size):
    width = browser_size.param[0]
    height = browser_size.param[1]

    browser.config.window_width = width
    browser.config.window_height = height

    browser.open(url)


@pytest.mark.parametrize("browser_size", [(1280, 1024)], indirect=True)
def test_github_desktop(browser_size):
    browser.element('a[href="/login"').click()
    browser.element(by.partial_text("Sign in")).should(be.visible)


@pytest.mark.parametrize("browser_size", [(320, 768)], indirect=True)
def test_github_mobile(browser_size):
    browser.element('[class="octicon octicon-three-bars"]').click()
    browser.element('a[href="/login"').click()
    browser.element(by.partial_text("Sign in")).should(be.visible)
