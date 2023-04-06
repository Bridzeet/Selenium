from selenium import webdriver
from logowanie import Buying
from selenium.webdriver.common.by import By
import time
from screenshot import make_screenshot
import pytest
from selenium.common.exceptions import NoSuchElementException

test_data = [
    ('wsb.spam@gmail.com', 'Projekt123#', 'https://www.reserved.com/pl/pl/'),
]

@pytest.mark.parametrize('username, password, url', test_data)
def test_login_page(username, password, url):
    driver = webdriver.Chrome()
    driver.get('https://www.reserved.com/pl/pl/')
    page = Buying(driver)
    page.click_cookie()
    time.sleep(3)
    konto = driver.find_element (By.CSS_SELECTOR, "div[data-testid*='account-info-logged-false']")
    konto.click()
    page.enter_username(username)
    page.enter_password(password)
    page.click_login()
    get_url = driver.current_url
    time.sleep(1)
    
    try:
        assert driver.current_url == url, make_screenshot(driver)
    finally:
        print('Udanych zakupów!')
        driver.quit()
