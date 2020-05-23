from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ObjectPageLocators

class PageObject(BasePage):

    def add_to_basket(self):
        button = self.browser.find_element(*ObjectPageLocators.BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    def add_to_basket_without_alert(self):
        button = self.browser.find_element(*ObjectPageLocators.BASKET_BUTTON)
        button.click()

    def should_be_object_in_basket(self):
        name = self.browser.find_element(*ObjectPageLocators.OBJECT_NAME)
        title = self.browser.find_element(*ObjectPageLocators.OBJECT_TITLE)
        assert title.text == name.text, "Wrong name of object in basket"

    def should_be_right_price(self):
        price_in_basket = self.browser.find_element(*ObjectPageLocators.OBJECT_PRICE_IN_BASKET)
        price = self.browser.find_element(*ObjectPageLocators.OBJECT_PRICE)
        assert price.text == price_in_basket.text, "Wrong price of object"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ObjectPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disapperead(*ObjectPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should be disappeared"

   