import pytest
from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login('admin', 'secret')
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login('admin', 'secret')
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def finalize():
        fixture.session.logout()
        fixture.complete()
    request.addfinalizer(finalize)
    return fixture