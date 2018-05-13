from model.data import Group

def test_add_group(app, json_groups):
    group = json_groups
    before = app.group.get_group_list()
    app.group.create(group)
    assert app.group.count() - len(before) == 1
    after = app.group.get_group_list()
    assert sorted(before, key=Group.id_or_max) != sorted(after, key=Group.id_or_max)
