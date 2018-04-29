from model.data import Contact


def test_add_contact(app):
    before = app.contact.get_contact_list()
    app.contact.create(Contact(firstname='firstname', lastname='lastname', nickname='nickname'))
    after = app.contact.get_contact_list()
    assert len(after) - 1 == len(before)
    assert after != before
