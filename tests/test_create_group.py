import pytest
from fixture.application import Application
from model.data import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.complete)
    return fixture


def test_add_group(app):
    app.session.login('admin', 'secret')
    app.group.create(Group(name='Test', header='Header', footer='Footer'))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login('admin', 'secret')
    app.group.create(Group('', '', ''))
    app.session.logout()
