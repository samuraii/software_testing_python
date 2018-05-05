import random
from model.data import Group


def test_edit_group_data(app):
    before = app.group.get_group_list()
    app.group.edit_data(Group(name='Test' + str(random.randint(1, 100)), header='New', footer='FooterNew'))
    assert len(before) == app.group.count()
    after = app.group.get_group_list()
    assert before != after, 'Список групп не изменился после редактирования данных группы'
