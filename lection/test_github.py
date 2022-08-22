import pytest
from selene import by
from selene.support.conditions import be
from selene.support.shared import browser

link = 'https://github.com'


@pytest.mark.parametrize("setup", [(1600, 900)], indirect=True)
def test_github_desktop(setup):
	browser.open(link)
	browser.element('a[href="/login').click()
	browser.element(by.text("Sign in to GitHub")).should(be.visible)


@pytest.mark.parametrize("setup", [(414, 896)], indirect=True)
def test_github_mobile(setup):
	browser.open(link)
	browser.element('[class="octicon octicon-three-bars"]').click()
	browser.element('[class="HeaderMenu-link flex-shrink-0 no-underline"]')
	browser.element(by.partial_text("Sign in")).should(be.visible)
