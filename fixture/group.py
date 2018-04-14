class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        self.app.wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
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
        self.return_to_group_page()

    def delete_first(self):
        wd = self.app.wd
        self.open_group_page()
        self.check_first()
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def check_number(self, number=0):
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[number].click()

    def edit_data(self, group_data, number=0):
        wd = self.app.wd
        self.open_group_page()
        self.check_number(number)
        wd.find_element_by_name("edit").click()
        if group_data.name:
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group_data.name)
        if group_data.header:
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group_data.header)
        if group_data.footer:
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group_data.footer)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        self.app.wd.find_element_by_link_text("group page").click()
