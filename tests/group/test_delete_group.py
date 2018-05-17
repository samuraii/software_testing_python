from model.data import Group
import random


def test_delete_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='Test', header='Header', footer='Footer'))
    before = db.get_group_list()
    group = random.choice(before)
    app.group.delete_by_id(group.id)
    assert (len(before) - 1) == app.group.count()
    after = db.get_group_list()
    assert sorted(before, key=Group.id_or_max) != sorted(after, key=Group.id_or_max)
    if check_ui:
        assert sorted(after, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
