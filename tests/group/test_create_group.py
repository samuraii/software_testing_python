from model.data import Group


def test_add_group(app):
    before = app.group.get_group_list()
    app.group.create(Group(name='Test', header='Header', footer='Footer'))
    assert app.group.count() - len(before) == 1
    after = app.group.get_group_list()
    assert before != after, 'Список групп не изменился после добавления группы'


def test_add_empty_group(app):
    before = app.group.get_group_list()
    app.group.create(Group('', '', ''))
    assert app.group.count() - len(before) == 1
    after = app.group.get_group_list()
    assert before != after, 'Список групп не изменился после добавления пустой группы'

