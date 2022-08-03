import pytest
from selene.support.shared import browser
import logging

logging.getLogger('WDM').setLevel(logging.NOTSET)

chrome = pytest.fixture(params=[(1600, 900), (414, 896)])

@chrome
def setup(request):
	return request


@pytest.fixture(scope='function', autouse=True)
def browser_settings(setup):
	browser.config.window_width = setup.param[0]
	browser.config.window_height = setup.param[1]