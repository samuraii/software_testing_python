import random
from model.data import Contact


def test_delete_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(
                firstname='firstname' + str(random.randint(1, 999)), 
                lastname='lastname', 
                nickname='nickname'))
    before = app.contact.get_contact_list()
    random_contact = random.randint(0, len(before) - 1)
    app.contact.delete_by_index(random_contact)
    app.accept_alert()
    assert (len(before) - 1) == app.contact.count()
    after = app.contact.get_contact_list()
    assert before != after
