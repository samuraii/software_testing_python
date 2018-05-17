from model.data import Contact


def test_add_contact(app, db, json_contacts):
    before = db.get_contact_list()
    app.contact.create(json_contacts)
    assert app.contact.count() - 1 == len(before)
    after = db.get_contact_list()
    assert sorted(before, key=Contact.id_or_max) != sorted(after, key=Contact.id_or_max)
