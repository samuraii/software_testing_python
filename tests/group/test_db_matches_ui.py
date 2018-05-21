from model.data import Group


def test_group_list_db_ui(app, db):
    ui_list = app.group.get_group_list()
    def clean_group(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean_group, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
