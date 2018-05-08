import random
from model.data import Contact


def test_edit_group_data(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='firstname' + str(random.randint(1, 999)), lastname='lastname', nickname='nickname'))
    before = app.contact.get_contact_list()
    random_contact = random.randint(0, len(before) - 1)
    rand_id = str(random.randint(1, 999))
    app.contact.edit_data_by_index(random_contact, Contact(firstname='firstname' + rand_id, lastname='lastname', nickname='nickname' + rand_id))
    assert app.contact.count() == len(before)
    after = app.contact.get_contact_list()
    assert after != before, 'Список контактов не изменился после редактирования контакта'
