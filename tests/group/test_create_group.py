from model.data import Group


def test_add_group(app):
    app.session.login('admin', 'secret')
    app.group.create(Group(name='Test', header='Header', footer='Footer'))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login('admin', 'secret')
    app.group.create(Group('', '', ''))
    app.session.logout()
