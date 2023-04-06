from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#REGISTER_account
driver = webdriver.Chrome()
driver.get('https://www.reserved.com/pl/pl/')
print('Nazwa strony',driver.title)
time.sleep(5)
konto = driver.find_element (By.CSS_SELECTOR, "div[data-testid*='account-info-logged-false']")
konto.click()
zaloz_konto = driver.find_element (By.CSS_SELECTOR, "[data-selen='register-select']")
zaloz_konto.click()
email = driver.find_element (By.ID, "email_id")
email.send_keys('wsb.spam@gmail.com')
imie = driver.find_element (By.ID, "firstname_id")
imie.send_keys('Spam')
nazwisko = driver.find_element (By.ID, "lastname_id")
nazwisko.send_keys('Testspam')
password_field = driver.find_element(By.ID, 'password_id')
password_field.send_keys('Projekt123#')
register = driver.find_element (By.CSS_SELECTOR, "button[data-selen*='create-account-submit']")
register.click()
time.sleep(1)
driver.get_screenshot_as_file('screenshot.png')
driver.quit()
       
 
    
   

   
  
