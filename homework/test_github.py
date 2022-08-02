import time
import pytest
from selene import by
from selene.support.conditions import be
from selene.support.shared import browser

link = 'https://github.com'


@pytest.mark.parametrize("window_size", ["400x817", "1600x900"])
@pytest.mark.parametrize("platform", [1, 2], ids=["Desktop", "Mobile"])
def test_github_selene(window_size, platform):
	browser.open(link)
	browser.element('[class="octicon octicon-three-bars"]').click()
	browser.element('[class="HeaderMenu-link flex-shrink-0 no-underline"]')
	time.sleep(1)
	browser.element(by.partial_text("Sign in")).should(be.visible)

