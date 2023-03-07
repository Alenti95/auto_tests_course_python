from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOG_IN = (By.CSS_SELECTOR, '[id="login_form"]')
    REGISTER = (By.CSS_SELECTOR, '[id="register_form"]')

class BasketPageLocators():
    BASKET = (By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main .price_color')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_BUSKET = (By.CSS_SELECTOR, '#messages > div > .alertinner p strong')
    NAME_BASKET = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div strong')