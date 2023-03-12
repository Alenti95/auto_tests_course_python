from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
import pytest


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        self.page = MainPage(browser, self.link)
        self.page.open()
        LoginPage(browser, browser.current_url).register_new_user('', '')
        BasePage(browser, browser.current_url).should_be_authorized_user()
        yield

    # Открываем страницу товара, Проверяем, что нет сообщения об успехе
    def test_user_cant_see_success_message(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = MainPage(browser, self.link)
        page.open()
        BasketPage(browser, browser.current_url).should_not_be_success_message()

    @pytest.mark.need_review
    # Открываем страницу, добавляем товар, проверяем название и цену в корзине
    def test_user_can_add_product_to_basket(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_add_product()
        BasketPage(browser, browser.current_url).should_be_price()
        BasketPage(browser, browser.current_url).should_be_name()
@pytest.mark.need_review
#Открываем страницу, добавляем товар, проверяем название и цену в корзине
@pytest.mark.parametrize('promo_offer', ["0","1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_add_product()
    page.solve_quiz_and_get_code()
    BasketPage(browser, browser.current_url).should_be_price()
    BasketPage(browser, browser.current_url).should_be_name()
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    BasketPage(browser, browser.current_url).basket_is_empty()  # корзина пуста
    BasketPage(browser, browser.current_url).basket_message_is_empty()  # проверка сообщения
@pytest.mark.need_review
#Открываем страницу, переходим на страницу логина
def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
