from selenium import webdriver
from selenium.webdriver.common.by import By
from logowanie import Buying
import time
import pytest
from selenium.common.exceptions import NoSuchElementException

test_data = [
    ('wsb.spam@gmail.com', 'Projekt123#','https://www.reserved.com/pl/pl/checkout/cart/')
]

@pytest.mark.parametrize('username, password, url', test_data)
def test_shopping(username, password, url):
    driver = webdriver.Chrome()
    page = Buying(driver)
    page.open()
    page.click_cookie()
    time.sleep(3)
    page.konto_button()
    page.enter_username(username)
    page.enter_password(password)
    page.click_log_button()
    time.sleep(5)
    page.kobieta_button()
    time.sleep(5)
    page.dla_niej_button()
    time.sleep(5)
    page.wybor_sukienki()
    time.sleep(5)
    page.size()
    time.sleep(5)
    page.choose_size_button()
    time.sleep(5)
    page.do_koszyka_button()
    time.sleep(5)
    page.zamowienie_button()
  
    if driver.current_url == url:
        driver.get_screenshot_as_file('screenshot.png')
        print("Zakupy się udały!")
    else:
        print("Zakupy się nie udały!")
        driver.quit()




                                                                     

  

