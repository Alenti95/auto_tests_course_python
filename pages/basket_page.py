from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_price_and_name(self):
        self.should_be_price()
        self.should_be_name()

    def should_be_price(self):
        assert self.is_element_present(*BasketPageLocators.PRICE_PRODUCT) == self.is_element_present(*BasketPageLocators.PRICE_BUSKET), 'Price is incorrect'
        assert True

    def should_be_name(self):
        assert self.is_element_present(*BasketPageLocators.NAME_PRODUCT) == self.is_element_present(*BasketPageLocators.NAME_BASKET), 'Name is incorrect'
        assert True