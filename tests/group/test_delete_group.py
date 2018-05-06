from model.data import Group
import random


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Test', header='Header', footer='Footer'))
    before = app.group.get_group_list()
    group_number = random.randint(0, len(before) - 1)
    app.group.delete_by_index(group_number)
    assert (len(before) - 1) == app.group.count()
    after = app.group.get_group_list()
    assert before != after
