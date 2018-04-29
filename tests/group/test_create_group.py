from model.data import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name='Test', header='Header', footer='Footer'))
    new_groups = app.group.get_group_list()
    assert len(new_groups) - len(old_groups) == 1


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group('', '', ''))
    new_groups = app.group.get_group_list()
    assert len(new_groups) - len(old_groups) == 1
