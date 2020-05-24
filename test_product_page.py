from .pages.product_page import PageObject
import time
import pytest

#@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
#def test_guest_can_add_product_to_basket(browser, promo_offer):
    #link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    #page = PageObject(browser, link) 
    #page.open()
    #page.add_to_basket()
    #page.should_be_object_in_basket()
    #page.should_be_right_price()

@pytest.mark.xfail(reason="right")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = PageObject(browser, link) 
    page.open()
    page.add_to_basket_without_alert()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser): 
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = PageObject(browser, link) 
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="right")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = PageObject(browser, link) 
    page.open()
    page.add_to_basket_without_alert()
    page.should_be_disappeared() 

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.go_to_login_page()
    
 

    
