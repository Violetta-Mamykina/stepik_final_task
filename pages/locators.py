from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password") 
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name = 'registration_submit']")

class ObjectPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    OBJECT_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    OBJECT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    OBJECT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    OBJECT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>.alert-success:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")