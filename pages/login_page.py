from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "'login' not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Login username is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration email is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "Registration password1 is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "Registration password2 is not presented"

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_form.send_keys(email)
        password1_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password1_form.send_keys(password)
        password2_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password2_form.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()
