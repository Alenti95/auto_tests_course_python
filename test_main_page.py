from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(5)
    login_page = LoginPage(browser, browser.current_url)
    time.sleep(5)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

#Открываем страницу, добавляем товар, проверяем название и цену в корзине
@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = MainPage(browser, link)
    page.open()
    page.go_to_add_product()
    page.solve_quiz_and_get_code()
    BasketPage(browser, browser.current_url).should_be_price()
    BasketPage(browser, browser.current_url).should_be_name()

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
