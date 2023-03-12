from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


#Добавляем товар в корзину, Проверяем, что нет сообщения об успехе
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1'
    page = MainPage(browser, link)
    page.open()
    page.go_to_add_product()
    page.solve_quiz_and_get_code()
    BasketPage(browser, browser.current_url).should_not_be_success_message()

#Открываем страницу товара, Проверяем, что нет сообщения об успехе
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1'
    page = MainPage(browser, link)
    page.open()
    BasketPage(browser, browser.current_url).should_not_be_success_message()

#Добавляем товар в корзину, Проверяем, что нет сообщения об успехе
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1'
    page = MainPage(browser, link)
    page.open()
    page.go_to_add_product()
    page.solve_quiz_and_get_code()
    BasketPage(browser, browser.current_url).should_not_be_success_message_disappear()

#Открываем страницу, видим переход на логин
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    page.basket_is_empty() #корзина пуста
    page.basket_message_is_empty() #проверка сообщения

