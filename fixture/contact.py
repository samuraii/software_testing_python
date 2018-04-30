from model.data import Contact


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

    def check_number(self, number=0):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_elements_by_name('selected[]')[number].click()

    def edit_data(self, contact_data, number=0):
        wd = self.app.wd
        self.check_number(number)
        wd.find_element_by_css_selector("img[title='Edit']").click()
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

    def delete(self, number=0):
        wd = self.wd
        self.check_number(number)
        wd.find_element_by_css_selector('input[value="Delete"]').click()

    def count(self):
        wd = self.wd
        self.app.open_homepage()
        return len(wd.find_elements_by_name('selected[]'))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_homepage()
        contacts = []
        for c in wd.find_elements_by_name('entry'):
            c_fields = c.find_elements_by_tag_name('td')
            lastname = c_fields[1].text
            firstname = c_fields[2].text
            id = c_fields[0].find_element_by_tag_name('input').get_attribute('id')
            contacts.append(Contact(id=id, firstname=lastname, lastname=firstname))
        return contacts
