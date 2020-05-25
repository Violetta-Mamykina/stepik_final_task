from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class PageBasket(BasePage):
    def should_be_message_about_empty_basket(self):
        message_empty = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET)
        assert "Your basket is empty." in message_empty.text, "Mistake in message about empty basket" 

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Items are in the basket"