import re
import random


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


# Проверяем что на главной станице отображаемая информация
# соответствует информации в БД
def test_credentials_on_home_page(app, orm):
    contacts_from_home_page = app.contact.get_contact_list()
    if len(contacts_from_home_page) == 0:
        app.contact.create_random_contact()
        contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = orm.get_contact_list()
    assert len(contacts_from_home_page) == len(contacts_from_db)
    
    for i in range(len(contacts_from_db)):
        assert contacts_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(
            contacts_from_db[i])
    
    for i in range(len(contacts_from_db)):
        assert contacts_from_home_page[i].all_phones_from_home_page == merge_emails_like_on_home_page(
        contacts_from_db[i])

    for i in range(len(contacts_from_db)):
        assert contacts_from_home_page[i].address == contacts_from_db[i].address

    for i in range(len(contacts_from_db)):
        assert contacts_from_db[i].firstname == contacts_from_home_page[i].firstname
        assert contacts_from_db[i].lastname == contacts_from_home_page[i].lastname


def test_credentials_on_view_page(app, orm):
    contacts_from_home_page = app.contact.get_contact_list()
    if len(contacts_from_home_page) == 0:
        app.contact.create_random_contact()
        contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = orm.get_contact_list()
    contact_amount = len(contacts_from_homepage)
    assert contact_amount == len(contacts_from_db)
    for i in range(len(contacts_from_db)):
        contact_from_view_page = app.contact.get_contact_info_from_view_page(i)
        assert merge_phones_like_on_home_page(contact_from_view_page) == merge_phones_like_on_home_page(
            contacts_from_db[i])
    # random email 
    random_index = random.randint(0, contact_amount - 1)
    contact_from_homepage = contacts_from_home_page[random_index]
    contact_from_view_page = app.contact.get_contact_info_from_view_page(random_index)
    assert contact_from_homepage.all_emails_from_home_page == contact_from_view_page.all_emails_from_view_page
    # random frist and last name
    random_index = random.randint(0, contact_amount - 1)
    contact_from_homepage = contacts_from_home_page[random_index]
    contact_from_view_page = app.contact.get_contact_info_from_view_page(random_index)
    assert contact_from_homepage.firstname == contact_from_view_page.firstname
    assert contact_from_homepage.lastname == contact_from_view_page.lastname


def test_credentials_on_edit_page(app):
    contacts_from_home_page = app.contact.get_contact_list()
    if len(contacts_from_home_page) == 0:
        app.contact.create_random_contact()
        contacts_from_home_page = app.contact.get_contact_list()
    contact_amount = len(app.contact.get_contact_list())
    random_index = random.randint(0, contact_amount - 1)
    contact_from_homepage = app.contact.get_contact_list()[random_index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(random_index)
    assert contact_from_homepage.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    # random address
    random_index = random.randint(0, contact_amount - 1)
    contact_from_homepage = contacts_from_home_page[random_index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(random_index)
    assert contact_from_homepage.address == contact_from_edit_page.address
    # random first and last name
    random_index = random.randint(0, contact_amount - 1)
    contact_from_homepage = contacts_from_home_page[random_index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(random_index)
    assert contact_from_homepage.firstname == contact_from_edit_page.firstname
    assert contact_from_homepage.lastname == contact_from_edit_page.lastname
