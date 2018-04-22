from model.data import Group


def test_add_group(app):
    app.group.create(Group(name='Test', header='Header', footer='Footer'))


def test_add_empty_group(app):
    app.group.create(Group('', '', ''))
