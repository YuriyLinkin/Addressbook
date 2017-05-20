from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from web_api.group_helper import GroupHelper
from web_api.session_helper import SessionHelper
from web_api.contact_helper import ContactHelper


class AddressBookAPI:
    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "edge":
            self.wd = webdriver.Edge()
        else:
            raise ValueError("Unrecognized browser {}".format(browser))


        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def open_homepage(self):
        wd = self.wd
        # open HomePage
        wd.get("http://localhost:8888/addressbook/")



    def destroy(self):
        self.wd.quit()

    def message(self):
        wd = self.wd
        return wd.find_element_by_css_selector("div.msgbox").text

    def is_element_present(self, by, locator):
        wd = self.wd
        try:
            wd.find_element(by, locator)
            return True
        except NoSuchElementException:
            return False


