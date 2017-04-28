from selenium import webdriver
import unittest

class updated_AB_api(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
    
    def test_updated_AB_api(self):

        self.open_site()
        self.login(password="secret", login="admin")
        self.open_groups()
        self.choose_changing_group()
        self.modify_group(name="Yuriy_group", header="header_y_group", footer="footer_y_group")
        self.updated_group()
        self.return_group_page()
        self.logout()

    def logout(self):
        # logout
        wd = self.wd
        wd.find_element_by_xpath("/html/body/div/div[1]/form/a").click()

    def return_group_page(self):
        # return_group _page
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def updated_group(self):
        # updated_group
        wd = self.wd
        wd.find_element_by_name("update").click()

    def modify_group(self, name, header, footer):
        # modify_group
        wd = self.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)

    def choose_changing_group(self):
        # choose_changing_group
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='content']/form").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/input[6]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/input[6]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[10]").click()

    def open_groups(self):
        # open_groups
        wd = self.wd
        wd.find_element_by_xpath("//*[@id='nav']/ul/li[3]/a").click()

    def login(self, login, password):
        # login
        wd = self.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_site(self):
        # open_site
        wd = self.wd
        wd.get("http://localhost:8888/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
