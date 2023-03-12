from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import BasePageLocators

class BasketPage(BasePage):

    def should_be_price(self):
        self.browser.implicitly_wait(10)
        assert self.browser.find_element(*BasketPageLocators.PRICE_PRODUCT).text == self.browser.find_element(*BasketPageLocators.PRICE_BUSKET).text, 'Price is incorrect'
        assert True

    def should_be_name(self):
        self.browser.implicitly_wait(10)
        assert self.browser.find_element(*BasketPageLocators.NAME_PRODUCT).text == self.browser.find_element(*BasketPageLocators.NAME_BASKET).text, 'Name is incorrect'
        assert True

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_disappear(self):
        assert self.is_disappeared(*BasketPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappear"

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasePageLocators.ITEM_1), 'basket is not empty'

    def basket_message_is_empty(self):
        assert "empty" in self.browser.find_element(*BasePageLocators.MESSAGE).text, 'basket is full'
