from model.data import Contact
import random


class ContactHelper:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def create(self, contact):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("submit").click()
        self.contact_cache = None

    def check_number(self, number=0):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_elements_by_name('selected[]')[number].click()
    
    def click_edit_contact(self, index):
        wd = self.app.wd
        wd.find_elements_by_css_selector("img[title='Edit']")[index].click()

    def edit_data_by_index(self, index, contact_data):
        wd = self.app.wd
        self.click_edit_contact(index)
        if contact_data.firstname:
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(contact_data.firstname)
        if contact_data.lastname:
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(contact_data.lastname)
        if contact_data.nickname:
            wd.find_element_by_name("nickname").click()
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(contact_data.nickname)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def delete_by_index(self, index):
        wd = self.wd
        self.check_number(index)
        wd.find_element_by_css_selector('input[value="Delete"]').click()
        self.contact_cache = None

    def count(self):
        wd = self.wd
        self.app.open_homepage()
        return len(wd.find_elements_by_name('selected[]'))

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
                contact_id = c_fields[0].find_element_by_tag_name('input').get_attribute('id')
                self.contact_cache.append(Contact(id=contact_id, firstname=lastname, lastname=firstname))
        return list(self.contact_cache)
