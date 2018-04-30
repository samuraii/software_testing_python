from model.data import Contact


def test_add_contact(app):
    before = app.contact.get_contact_list()
    app.contact.create(Contact(firstname='firstname', lastname='lastname', nickname='nickname'))
    assert app.contact.count() - 1 == len(before)
    after = app.contact.get_contact_list()
    assert after != before, 'Список контактов не изменился после добавления контакта'
