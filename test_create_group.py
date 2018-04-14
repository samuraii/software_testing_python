import pytest
from application import Application
from data import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.complete)
    return fixture


def test_add_group(app):
    app.login('admin', 'secret')
    app.create_group(Group(name='Test', header='Header', footer='Footer'))
    app.logout()


def test_add_empty_group(app):
    app.login('admin', 'secret')
    app.create_group(Group('', '', ''))
    app.logout()
