import pytest
from model.data import Group
from data.add_group import testdata

@pytest.mark.parametrize('group', testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    before = app.group.get_group_list()
    app.group.create(group)
    assert app.group.count() - len(before) == 1
    after = app.group.get_group_list()
    assert sorted(before, key=Group.id_or_max) != sorted(after, key=Group.id_or_max)
