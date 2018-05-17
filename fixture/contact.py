from model.data import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

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
