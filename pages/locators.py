from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BTN = (By.CSS_SELECTOR, "div.basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")
    EMAIL_INPUT_ON_REGISTER_FORM = (By.CSS_SELECTOR, "input#id_registration-email")
    PASSWORD1_INPUT_ON_REGISTER_FORM = (By.CSS_SELECTOR, "input#id_registration-password1")
    PASSWORD2_INPUT_ON_REGISTER_FORM = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, "form#register_form button")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "div.alert-success strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")


class BasketPageLocators:
    BASKET_ITEMS_DIV = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "div#content_inner p")
