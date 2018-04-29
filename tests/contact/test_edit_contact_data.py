import random
from model.data import Contact


def test_edit_group_data(app):
    name = random.randint(1, 100)
    before = app.contact.get_contact_list()
    app.contact.edit_data(Contact(firstname='firstname{}'.format(name), lastname='lastname', nickname='nickname{}'.format(name)))
    after = app.contact.get_contact_list()
    assert len(after) == len(before)
    assert after != before