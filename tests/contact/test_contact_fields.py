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

def test_contact_phones_on_edit_page(app):
    contact_amount = len(app.contact.get_contact_list())
    random_index = random.randint(0, contact_amount - 1)
    contact_from_homepage = app.contact.get_contact_list()[random_index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(random_index)
    assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_contact_phones_on_view_page(app):
    contact_amount = len(app.contact.get_contact_list())
    random_index = random.randint(0, contact_amount - 1)
    contact_from_homepage = app.contact.get_contact_list()[random_index]
    contact_from_view_page = app.contact.get_contact_info_from_view_page(random_index)
    assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_view_page)


def test_emails_on_edit_page(app):
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
