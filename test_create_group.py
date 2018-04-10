from selenium.webdriver.chrome.webdriver import WebDriver
import unittest
from group import Group


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.success = True

    def open_homepage(self, wd):
        wd.get("http://localhost/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def create_group(self, wd, group):
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_css_selector("span.group").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def complete(self, wd):
        wd.quit()

    def test_add_group(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, 'admin', 'secret')
        self.open_group_page(wd)
        self.create_group(wd, Group(name='Test', header='Header', footer='Footer'))
        self.return_to_group_page(wd)
        self.logout(wd)
        self.complete(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, 'admin', 'secret')
        self.open_group_page(wd)
        self.create_group(wd, Group('', '', ''))
        self.return_to_group_page(wd)
        self.logout(wd)
        self.complete(wd)


if __name__ == '__main__':
    unittest.main()
