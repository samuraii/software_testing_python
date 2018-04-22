from model.data import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname='firstname', lastname='lastname', nickname='nickname'))
