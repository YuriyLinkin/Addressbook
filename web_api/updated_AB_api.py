from selenium import webdriver
import unittest

class updated_AB_api(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
    
    def test_updated_AB_api(self):
        wd = self.wd
        #open_site
        wd.get("http://localhost:8888/addressbook/")
        #login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        #open_groups
        wd.find_element_by_link_text("//*[@id='nav']/ul/li[3]/a").click()
        #choose_changing_group
        wd.find_element_by_xpath("//div[@id='content']/form").click()
        if not wd.find_element_by_name("selected[]").is_selected():
            wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[9]").click()
        #modify_group
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("group_byYuriy")
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("group_byYuriy")

        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("header")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("header_byYuriy")

        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("footer")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("footer_byYuriy")
        #updated_group
        wd.find_element_by_name("update").click()
        #return_group _page
        wd.find_element_by_link_text("group page").click()
        #logout
        wd.find_element_by_link_text("form[name='logout'] > a").click()

    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
