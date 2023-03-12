from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in current url"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_IN), "Log_in form  is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER), "Register form  is not presented"
        assert True

    def register_new_user(self, email, password):
        self.email = f'{str(time.time()) + "@fakemail.org"}'
        self.password = f'{str(time.time()) + str(time.time())}'
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(self.email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_1).send_keys(self.password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_2).send_keys(self.password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER).click()