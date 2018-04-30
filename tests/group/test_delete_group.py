from model.data import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Test', header='Header', footer='Footer'))
    before = app.group.get_group_list()
    app.group.delete_first()
    assert (len(before) - 1) == app.group.count()
    after = app.group.get_group_list()
    before[0:1] = []
    assert before == after
