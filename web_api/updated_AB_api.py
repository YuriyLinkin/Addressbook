from selenium import webdriver


class AddressBookAPI_2:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
    


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
        self.open_site()
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

    def exit(self):
        self.wd.quit()

    def message(self):
        wd = self.wd
        return wd.find_element_by_css_selector("div.msgbox").text


