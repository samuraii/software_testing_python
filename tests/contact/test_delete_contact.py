from model.data import Contact


def test_delete_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='firstname', lastname='lastname', nickname='nickname'))
    before = app.contact.get_contact_list()
    app.contact.delete()
    app.accept_alert()
    assert app.contact.count() + 1 == len(before)
    after = app.contact.get_contact_list()
    before[0:1] = []
    assert before == after
