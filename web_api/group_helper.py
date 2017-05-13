from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of, element_to_be_clickable

from selenium.webdriver.common.by import By
from models.group import Group

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_page(self):
        wd = self.app.wd
        # Open GroupPage
        group_link = wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[3]/a")
        group_link.click()
        WebDriverWait(wd, 15).until(staleness_of(group_link))

    def create_group(self, group):
        wd = self.app.wd
        # Init Group form
        button = wd.find_element_by_name("new")
        button.click()
        WebDriverWait(wd, 15).until(staleness_of(button))

        if group.name_group is not None:
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group.name_group)
        if group.header_group is not None:
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group.header_group)
        if group.footer_group is not None:
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group.footer_group)

        # Submit groupForm
        wd.find_element_by_name("submit").click()

    def return_group_page(self):
        wd = self.app.wd
        # Return GroupPage
        bb = wd.find_element_by_link_text("group page")
        bb.click()
        WebDriverWait(wd, 15).until(staleness_of(bb))

    def delete_group_by_number(self, number):

        wd = self.app.wd
        # open_page()
        checkboxes = wd.find_elements_by_name("selected[]")
        checkboxes[number].click()
        wd.find_element_by_name("delete").click()
    """""
    def delete_groups_all(self):

        wd = self.app.wd
        # open_page()
        checkboxes = wd.find_elements_by_name("selected[]")
        for i in checkboxes:
            i.click()
        wd.find_element_by_name("delete").click()
    """

    def is_groups_present(self):
        self.open_page()
        return self.app.is_element_present(By.NAME, 'selected[]')

    def get_list(self):
        wd = self.app.wd
        self.open_page()
        checkboxes = wd.find_elements_by_name('selected[]')
        groups = []
        for checkbox in checkboxes:
            name = checkbox.get_attribute('title')[8:-1]
            id = int(checkbox.get_attribute('value'))
            Group(name_group=name, id=id)
            groups.append(Group(name_group=name, id=id))
        return groups

    def count(self):
        wd = self.app.wd
        self.open_page()
        checkboxes = wd.find_elements_by_name('selected[]')
        return len(checkboxes)

    def modification_by_number(self, number, data_to_modification ):
        data_to_modification.name
        data_to_modification.footer
        data_to_modification.header
