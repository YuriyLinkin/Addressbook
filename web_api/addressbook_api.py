from selenium import webdriver

class AddressBookAPI:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(5)

    def open_homepage(self):
        wd = self.wd
        # open HomePage
        wd.get("http://localhost:8888/addressbook/")

    def login(self, password="secret", login="admin"):
        wd = self.wd
        self.open_homepage()
        # Login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath('//*[@id="LoginForm"]/input[3]').click()

    def open_page(self):
        wd = self.wd
        # Open GroupPage
        wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[3]/a").click()

    def create_group(self, group):
        wd = self.wd
        # Init Group form
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name_group)

        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header_group)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer_group)

        # Submit groupForm
        wd.find_element_by_name("submit").click()

    def return_group_page(self):
        wd = self.wd
        # Return GroupPage
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        wd = self.wd
        # Logout
        wd.find_element_by_xpath("/html/body/div/div[1]/form/a").click()

    def destroy(self):
        self.wd.quit()

    def delete_group_by_number(self, number):

        wd = self.wd
        # open_page()
        checkboxes = wd.find_elements_by_name("selected[]")
        checkboxes[number].click()
        wd.find_element_by_name("delete").click()

    def message(self):
        wd = self.wd
        return wd.find_element_by_css_selector("div.msgbox").text

