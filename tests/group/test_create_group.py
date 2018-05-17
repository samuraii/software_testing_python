from model.data import Group

def test_add_group(app, db, json_groups):
    group = json_groups
    before = db.get_group_list()
    app.group.create(group)
    after = db.get_group_list()
    assert sorted(before, key=Group.id_or_max) != sorted(after, key=Group.id_or_max)
