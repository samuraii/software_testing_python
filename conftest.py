import pytest
from fixture.application import Application

fixture = None



@pytest.fixture
def app(request):
    global fixture
    browser = pytest.config.getoption('--browser')
    url = pytest.config.getoption('--url')
    if fixture is None:
        fixture = Application(browser=browser, url=url)
        fixture.session.login('admin', 'secret')
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, url=url)
    fixture.session.ensure_login('admin', 'secret')
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def finalize():
        fixture.session.logout()
        fixture.complete()
    request.addfinalizer(finalize)
    return fixture


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', action='store')
    parser.addoption('--url', default='http://localhost/', action='store')
