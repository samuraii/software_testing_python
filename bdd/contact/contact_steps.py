from pytest_bdd import given, when, then
from model.data import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <firstname>, <lastname> and <nickname>')
def new_contact(firstname, lastname, nickname):
    return Contact(firstname=firstname, lastname=lastname, nickname=nickname)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('The new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max() == sorted(new_contacts, key=Contact.id_or_max()))


@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create_random_contact()
    return db.get_contact_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_by_id(random_contact.id)


@then('the new contact list is equal to the old list without the deleted contact')
def verify_contact_deleted(db, app, non_empty_contact_list, random_contact, check_ui):
    before = non_empty_contact_list
    app.contact.delete_by_id(random_contact)
    assert (len(before) - 1) == app.contact.count()
    after = db.get_contact_list()
    assert sorted(before, key=Contact.id_or_max) != sorted(after, key=Contact.id_or_max)
    if check_ui:
        assert sorted(after, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


@when('I modify the contact from the list with random strings')
def modify_contact(app, non_empty_contact_list):
    before = non_empty_contact_list
    random_contact = random.randint(0, len(before) - 1)
    rand_id = str(random.randint(1, 999))
    app.contact.edit_data_by_index(random_contact,
                                   Contact(firstname='firstname' + rand_id, lastname='lastname' + rand_id,
                                           nickname='nickname' + rand_id))


@then('The new contact list is equal to the old contact list with edited contact')
def verify_contact_list(app, non_empty_contact_list):
    before = non_empty_contact_list
    assert app.contact.count() == len(before)
    after = app.contact.get_contact_list()
    assert after != before, 'Список контактов не изменился после редактирования контакта'
