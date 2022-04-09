from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_is_empty_message(self):
        basket_is_empty_text = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_TEXT).text
        assert basket_is_empty_text == "Your basket is empty. Continue shopping", \
            "Basket is empty message isn't presented, but should be"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_DIV), \
            "Items in basket is presented, but should not be"
