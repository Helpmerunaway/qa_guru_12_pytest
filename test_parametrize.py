import pytest
from selene import by, be
from selene.support.shared import browser

url = 'https://github.com'


@pytest.fixture(scope='function', params=[(1600, 900), (1280, 1024)])
def browser_settings_desktop(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    browser.open(url)


def test_github_desktop(browser_settings_desktop):
    browser.element('a[href="/login"').click()
    browser.element(by.partial_text("Sign in")).should(be.visible)


@pytest.fixture(scope='function', params=[(414, 896), (320, 768)])
def browser_settings_mobile(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    browser.open(url)


def test_github_mobile(browser_settings_mobile):
    browser.element('[class="octicon octicon-three-bars"]').click()
    browser.element('a[href="/login"').click()
    browser.element(by.partial_text("Sign in")).should(be.visible)
