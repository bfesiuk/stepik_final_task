import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_added_product_to_basket(self):
        self.add_product_to_basket()
        self.should_be_equal_name_on_product_page_and_in_basket()
        self.should_be_equal_price_on_product_page_and_in_basket()
        self.should_disappeared_after_adding_product_to_basket()

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()
        self.solve_quiz_and_get_code()

    def should_be_equal_name_on_product_page_and_in_basket(self):
        product_name_on_product_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PRODUCT_PAGE).text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert product_name_in_basket == product_name_on_product_page, \
            "Product didn't added to basket: product name isn't equal in basket"

    def should_be_equal_price_on_product_page_and_in_basket(self):
        product_price_on_product_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ON_PRODUCT_PAGE).text
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert product_price_in_basket == product_price_on_product_page, \
            "Product didn't added to basket: product price isn't equal in basket"

    def should_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message isn't disappeared after adding, but should not be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
