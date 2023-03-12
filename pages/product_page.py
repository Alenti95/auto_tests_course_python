from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage
from .locators import BasketPageLocators
class ProductPage(BasePage):
    def go_to_add_product(self):
        basket = self.browser.find_element(*BasketPageLocators.BASKET)
        basket.click()