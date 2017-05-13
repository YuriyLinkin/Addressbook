from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of, element_to_be_clickable

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, password, login):
        wd = self.app.wd
        self.app.open_homepage()
        # Login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        #[wd.find_element_by_xpath('//*[@id="LoginForm"]/input[3]').click()]
        button = wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]")
        button.click()
        WebDriverWait(wd, 15).until(staleness_of(button))

    def logout(self):
        wd = self.app.wd
        # Logout
                    #[wd.find_element_by_xpath("/html/body/div/div[1]/form/a").click()]
        link = WebDriverWait(wd, 15).until(element_to_be_clickable((By.CSS_SELECTOR, 'form[name="logout"] > a')))
        link.click()
