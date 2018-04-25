from model.data import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Test', header='Header', footer='Footer'))
    app.group.delete_first()
