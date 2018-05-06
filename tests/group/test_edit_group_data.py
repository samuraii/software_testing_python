import random
from model.data import Group


def test_edit_group_data(app):
    before = app.group.get_group_list()
    random_group = random.randint(0, len(before) - 1)
    app.group.edit_data_by_index(random_group, Group(name='Test' + str(random.randint(1, 100)), header='New', footer='FooterNew'))
    assert len(before) == app.group.count()
    after = app.group.get_group_list()
    assert before != after, 'Список групп не изменился после редактирования данных группы'
