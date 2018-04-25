from model.data import Contact


def test_delete_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='firstname', lastname='lastname', nickname='nickname'))
    app.contact.delete()
    app.accept_alert()
