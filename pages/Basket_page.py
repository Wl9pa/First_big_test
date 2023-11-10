from .locators import BasketPageLocators
from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM), \
            "Basket form is presented, but should not be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "Message about empty basket is not presented, but should be"
