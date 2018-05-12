import random
import pytest
import string
from model.data import Group


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(max_len))])


testdata = [Group('', '', '')] + [
    Group(name=random_string('name', 10), header=random_string('header', 10), footer=random_string('footer', 10))
    for i in range(5)
]


@pytest.mark.parametrize('group', testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    before = app.group.get_group_list()
    app.group.create(group)
    assert app.group.count() - len(before) == 1
    after = app.group.get_group_list()
    assert before != after, 'Список групп не изменился после добавления группы'
