from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOG_IN = (By.CSS_SELECTOR, '[id="login_form"]')
    REGISTER = (By.CSS_SELECTOR, '[id="register_form"]')