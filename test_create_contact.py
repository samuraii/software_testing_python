import pytest
from application import Application
from data import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.complete)
    return fixture


def test_add_contact(app):
    app.login('admin', 'secret')
    app.create_contact(Contact(firstname='firstname', lastname='lastname', nickname='nickname'))
    app.logout()
