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

    def delete_all(self):
        wd = self.wd
        wd.find_element_by_css_selector('input[id="MassCB"]').click()
        wd.find_element_by_css_selector('input[value="Delete"]').click()
