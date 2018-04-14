import pytest
from fixture.application import Application
from model.data import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.complete)
    return fixture


def test_add_contact(app):
    app.session.login('admin', 'secret')
    app.contact.create(Contact(firstname='firstname', lastname='lastname', nickname='nickname'))
    app.contact.delete_all()
    app.accept_alert()
    app.session.logout()
