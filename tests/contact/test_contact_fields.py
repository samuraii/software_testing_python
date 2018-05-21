import re
import random
from data.contacts import Contact, random_string, random_phone


def clear_phone_from_additional_symbols(phone):
    return re.sub('[() -]', "", phone)


def merge_phones_like_on_home_page(contact):
    return '\n'.join(
        filter(lambda phone: phone != '',
               map(lambda phone: clear_phone_from_additional_symbols(phone),
                   filter(lambda phone: phone is not None,
                          [
                              contact.home_phone,
                              contact.mobile_phone,
                              contact.work_phone,
                              contact.secondary_phone
                          ]
                          )
                   )
               )
    )


def merge_emails_like_on_home_page(contact):
    return '\n'.join(
        filter(lambda email: email != '',
               filter(lambda email: email is not None,
                      [
                          contact.email,
                          contact.email2,
                          contact.email3
                      ]
                      )
               )
    )


def create_random_contact(app_instance):
    app_instance.contact.create(
        Contact(
            firstname=random_string('firstname', 10),
            lastname=random_string('lastname', 15),
            nickname=random_string('nickname', 15),
            email=random_string('e', 10, 0) + '@mail.ru',
            home_phone=random_phone(8),
            mobile_phone=random_phone(8),
            secondary_phone=random_phone(8),
            work_phone=random_phone(8)
        )
    )


# Проверяем что на главной станице отображаемая информация
# соответствует информации в БД
def test_contact_phones_on_home_page(app, orm):
    contacts_from_home_page = app.contact.get_contact_list()
    if len(contacts_from_home_page) == 0:
        create_random_contact(app_instance=app)
    contacts_from_db = orm.get_contact_list()
    assert len(contacts_from_home_page) == len(contacts_from_db)
    for i in range(len(contacts_from_db)):
        assert contacts_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(
            contacts_from_db[i])


def test_emails_on_home_page(app, orm):
    contacts_from_home_page = app.contact.get_contact_list()
    if len(contacts_from_home_page) == 0:
        create_random_contact(app_instance=app)
    contacts_from_db = orm.get_contact_list()
    assert len(contacts_from_home_page) == len(contacts_from_db)
    for i in range(len(contacts_from_db)):
        assert contacts_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(
            contacts_from_db[i])


def test_address_on_home_page(app, orm):
    contacts_from_home_page = app.contact.get_contact_list()
    if len(contacts_from_home_page) == 0:
        create_random_contact(app_instance=app)
    contacts_from_db = orm.get_contact_list()
    assert len(contacts_from_home_page) == len(contacts_from_db)
    for i in range(len(contacts_from_db)):
        assert contacts_from_home_page[i].address == contacts_from_db[i].address


def test_first_and_last_name_on_home_page(app, orm):
    contacts_from_home_page = app.contact.get_contact_list()
    if len(contacts_from_home_page) == 0:
        create_random_contact(app_instance=app)
    contacts_from_db = orm.get_contact_list()
    assert len(contacts_from_home_page) == len(contacts_from_db)
    for i in range(len(contacts_from_db)):
        assert contacts_from_db[i].firstname == contacts_from_home_page[i].firstname
        assert contacts_from_db[i].lastname == contacts_from_home_page[i].lastname


def test_contact_phones_on_view_page(app, orm):
    contacts_from_home_page = app.contact.get_contact_list()
    if len(contacts_from_home_page) == 0:
        create_random_contact(app_instance=app)
    contacts_from_db = orm.get_contact_list()
    assert len(contacts_from_home_page) == len(contacts_from_db)
    for i in range(len(contacts_from_db)):
        contact_from_view_page = app.contact.get_contact_info_from_view_page(i)
        assert merge_phones_like_on_home_page(contact_from_view_page) == merge_phones_like_on_home_page(
            contacts_from_db[i])


def test_emails_on_edit_page(app):
    contacts_from_home_page = app.contact.get_contact_list()
    if len(contacts_from_home_page) == 0:
        create_random_contact(app_instance=app)
    contact_amount = len(app.contact.get_contact_list())
    random_index = random.randint(0, contact_amount - 1)
    contact_from_homepage = app.contact.get_contact_list()[random_index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(random_index)
    assert contact_from_homepage.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_emails_on_view_page(app):
    contact_amount = len(app.contact.get_contact_list())
    random_index = random.randint(0, contact_amount - 1)
    contact_from_homepage = app.contact.get_contact_list()[random_index]
    contact_from_view_page = app.contact.get_contact_info_from_view_page(random_index)
    assert contact_from_homepage.all_emails_from_home_page == contact_from_view_page.all_emails_from_view_page


def test_address_on_edit_page(app):
    contact_amount = len(app.contact.get_contact_list())
    random_index = random.randint(0, contact_amount - 1)
    contact_from_homepage = app.contact.get_contact_list()[random_index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(random_index)
    assert contact_from_homepage.address == contact_from_edit_page.address


def test_first_and_last_name_on_edit_page(app):
    contact_amount = len(app.contact.get_contact_list())
    random_index = random.randint(0, contact_amount - 1)
    contact_from_homepage = app.contact.get_contact_list()[random_index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(random_index)
    assert contact_from_homepage.firstname == contact_from_edit_page.firstname
    assert contact_from_homepage.lastname == contact_from_edit_page.lastname


def test_first_and_last_name_on_view_page(app):
    contact_amount = len(app.contact.get_contact_list())
    random_index = random.randint(0, contact_amount - 1)
    contact_from_homepage = app.contact.get_contact_list()[random_index]
    contact_from_view_page = app.contact.get_contact_info_from_view_page(random_index)
    assert contact_from_homepage.firstname == contact_from_view_page.firstname
    assert contact_from_homepage.lastname == contact_from_view_page.lastname
