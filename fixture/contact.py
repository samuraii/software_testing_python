from model.data import Contact, Group
from fixture.group import GroupHelper
from data.contacts import random_string, random_phone
from selenium.webdriver.support.select import Select
import re
import random


class ContactHelper:

    def __init__(self, app, orm):
        self.app = app
        self.orm = orm
        self.wd = self.app.wd
        self.group = GroupHelper()

    def create(self, contact):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        if contact.firstname:
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(contact.firstname)
        if contact.lastname:
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(contact.lastname)
        if contact.nickname:
            wd.find_element_by_name("nickname").click()
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(contact.nickname)
        if contact.address:
            wd.find_element_by_name("address").click()
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(contact.nickname)
        if contact.email:
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(contact.email)
        if contact.email2:
            wd.find_element_by_name("email2").click()
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys(contact.email2)
        if contact.email3:
            wd.find_element_by_name("email3").click()
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys(contact.email3)
        if contact.home_phone:
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(contact.home_phone)
        if contact.mobile_phone:
            wd.find_element_by_name("mobile").click()
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        if contact.work_phone:
            wd.find_element_by_name("work").click()
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(contact.work_phone)
        if contact.secondary_phone:
            wd.find_element_by_name("phone2").click()
            wd.find_element_by_name("phone2").clear()
            wd.find_element_by_name("phone2").send_keys(contact.secondary_phone)
        wd.find_element_by_name("submit").click()
        self.contact_cache = None

    def create_random_contact(self):
        self.create(
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

    def click_edit_contact(self, index):
        wd = self.wd
        wd.find_elements_by_css_selector("img[title='Edit']")[index].click()

    def edit_data_by_index(self, index, contact):
        wd = self.wd
        self.click_edit_contact(index)
        if contact.firstname:
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(contact.firstname)
        if contact.lastname:
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(contact.lastname)
        if contact.nickname:
            wd.find_element_by_name("nickname").click()
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(contact.nickname)
        if contact.address:
            wd.find_element_by_name("address").click()
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(contact.nickname)
        if contact.email:
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(contact.email)
        if contact.email2:
            wd.find_element_by_name("email2").click()
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys(contact.email2)
        if contact.email3:
            wd.find_element_by_name("email3").click()
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys(contact.email3)
        if contact.home_phone:
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(contact.home_phone)
        if contact.mobile_phone:
            wd.find_element_by_name("mobile").click()
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        if contact.work_phone:
            wd.find_element_by_name("work").click()
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(contact.work_phone)
        if contact.secondary_phone:
            wd.find_element_by_name("phone2").click()
            wd.find_element_by_name("phone2").clear()
            wd.find_element_by_name("phone2").send_keys(contact.secondary_phone)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def delete_by_id(self, id):
        wd = self.wd
        wd.find_element_by_id('{}'.format(id)).click()
        wd.find_element_by_css_selector('input[value="Delete"]').click()
        self.contact_cache = None

    def check_contact(self, number):
        wd = self.wd
        wd.find_element_by_css_selector('input[value="{}"]'.format(number)).click()

    def count(self):
        wd = self.wd
        self.app.open_homepage()
        return len(wd.find_elements_by_name('entry'))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_homepage()
            self.contact_cache = []
            for c in wd.find_elements_by_name('entry'):
                c_fields = c.find_elements_by_tag_name('td')
                lastname = c_fields[1].text
                firstname = c_fields[2].text
                all_phones = c_fields[5].text
                all_emails = c_fields[4].text
                address = c_fields[3].text
                contact_id = c_fields[0].find_element_by_tag_name('input').get_attribute('id')
                self.contact_cache.append(
                    Contact(
                        id=contact_id,
                        firstname=firstname,
                        lastname=lastname,
                        all_phones_from_home_page=all_phones,
                        all_emails_from_home_page=all_emails,
                        address=address
                    )
                )
        return self.contact_cache

    def get_contact_info_from_edit_page(self, index):
        wd = self.wd
        self.click_edit_contact(index)
        id = wd.find_element_by_name('id').get_attribute('value')
        first_name = wd.find_element_by_name('firstname').get_attribute('value')
        last_name = wd.find_element_by_name('lastname').get_attribute('value')
        nick_name = wd.find_element_by_name('nickname').get_attribute('value')
        home_phone = wd.find_element_by_name('home').get_attribute('value')
        mobile_phone = wd.find_element_by_name('mobile').get_attribute('value')
        work_phone = wd.find_element_by_name('work').get_attribute('value')
        secondary_phone = wd.find_element_by_name('phone2').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        return Contact(
            id=id,
            firstname=first_name,
            lastname=last_name,
            nickname=nick_name,
            home_phone=home_phone,
            work_phone=work_phone,
            mobile_phone=mobile_phone,
            secondary_phone=secondary_phone,
            email=email,
            email2=email2,
            email3=email3,
            address=address
        )

    def open_contact_view_page(self, index):
        wd = self.wd
        entry = wd.find_elements_by_name('entry')[index]
        entry.find_elements_by_tag_name('td')[6].find_element_by_tag_name('a').click()

    def get_contact_info_from_view_page(self, index):
        wd = self.wd
        self.open_contact_view_page(index)
        text = wd.find_element_by_id('content').text

        first_last_name = wd.find_element_by_id('content').find_element_by_tag_name('b').text

        try:
            home_phone = re.search('H: (.*)', text).group(1)
        except AttributeError:
            home_phone = ''

        try:
            work_phone = re.search('W: (.*)', text).group(1)
        except AttributeError:
            work_phone = ''

        try:
            mobile_phone = re.search('M: (.*)', text).group(1)
        except AttributeError:
            mobile_phone = ''

        try:
            secondary_phone = re.search('P: (.*)', text).group(1)
        except AttributeError:
            secondary_phone = ''

        emails = re.findall('[A-Zaa-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)
        all_mails = '\n'.join(emails)

        return Contact(
            firstname=first_last_name.split()[0],
            lastname=first_last_name.split()[1],
            home_phone=home_phone,
            work_phone=work_phone,
            mobile_phone=mobile_phone,
            secondary_phone=secondary_phone,
            all_emails_from_view_page=all_mails
        )

    def add_to_group(self):
        wd = self.app.wd
        available_groups = self.orm.get_group_list()
        if len(available_groups) == 0:
            self.group.create(Group(name='ToTest', header='ToTestHeader', footer='ToTestFooter'))
            available_groups = self.orm.get_group_list()
        self.app.open_homepage()
        available_contacts = self.orm.get_contact_list()
        if len(available_contacts) == 0:
            self.create_random_contact()
            available_contacts = self.orm.get_contact_list()
        contact_index = random.randint(0, len(available_contacts))
        added_contact = self.get_contact_info_from_edit_page(contact_index)
        self.check_contact(contact_index)
        group_to_add = Select(wd.find_element_by_name('to_group')).first_selected_option()
        wd.find_element_by_name('add').click()
        self.app.open_homepage()
        return {'added_contact': added_contact, 'group_to_add': group_to_add}

    def remove_contact_from_group(self, group):
        wd = self.app.wd
        Select(wd.find_element_by_name('group')).select_by_visible_text(group.name)
        contacts = self.get_contact_list()
        random_index = random.randint(0, len(contacts))
        contact_to_delete = contacts[random_index]
        self.check_contact(random_index)
        wd.find_element_by_name('remove').click()
        self.app.open_homepage()
        return contact_to_delete
