from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_price_and_name(self):
        self.should_be_price()
        self.should_be_name()

    def should_be_price(self):
        assert self.browser.find_element(*BasketPageLocators.PRICE_PRODUCT).text == self.browser.find_element(*BasketPageLocators.PRICE_BUSKET).text, 'Price is incorrect'
        assert True

    def should_be_name(self):
        assert self.browser.find_element(*BasketPageLocators.NAME_PRODUCT).text == self.browser.find_element(*BasketPageLocators.NAME_BASKET).text, 'Name is incorrect'
        assert True