from selenium import webdriver
import unittest

class updated_AB_api(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
    
    def test_updated_AB_api(self):
        wd = self.wd
        self.open_site(wd)
        self.login(wd)
        self.open_groups(wd)
        self.choose_changing_group(wd)
        self.modify_group(wd)
        self.updated_group(wd)
        self.return_group_page(wd)
        self.logout(wd)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("form[name='logout'] > a").click()

    def return_group_page(self, wd):
        # return_group _page
        wd.find_element_by_link_text("group page").click()

    def updated_group(self, wd):
        # updated_group
        wd.find_element_by_name("update").click()

    def modify_group(self, wd):
        # modify_group
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("Yuriy_group")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("header_y_group")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("footer_y_group")

    def choose_changing_group(self, wd):
        # choose_changing_group
        wd.find_element_by_xpath("//div[@id='content']/form").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/input[6]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/input[6]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[10]").click()

    def open_groups(self, wd):
        # open_groups
        wd.find_element_by_xpath("//*[@id='nav']/ul/li[3]/a").click()

    def login(self, wd):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_site(self, wd):
        # open_site
        wd.get("http://localhost:8888/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
