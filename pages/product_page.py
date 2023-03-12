from .base_page import BasePage
from .locators import BasketPageLocators
class ProductPage(BasePage):
    def go_to_add_product(self):
        basket = self.browser.find_element(*BasketPageLocators.BASKET)
        basket.click()