from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException

from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.homepage = 'http://localhost/'

    def is_valid(self):
        try:
            url = self.wd.current_url
            return True
        except:
            return False

    def accept_alert(self):
        try:
            self.wd.switch_to_alert().accept()
        except NoAlertPresentException:
            pass

    def open_homepage(self):
        if not (self.wd.current_url == self.homepage):
            self.wd.get(self.homepage)

    def complete(self):
        self.wd.quit()
