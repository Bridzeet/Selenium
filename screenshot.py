from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.common.exceptions import NoSuchElementException


def make_screenshot(driver):
    teraz = datetime.datetime.now()
    screenshot = 'screenshot' + teraz.strftime('_%H%M%S') + '.png'
    driver.get_screenshot_as_file(screenshot)
