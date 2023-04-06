from selenium import webdriver
from selenium.webdriver.common.by import By

class Buying:
    def __init__(self, driver):
        self.driver = driver
        self.username_field_id = "login[username]_id"
        self.password_field_id = "login[password]_id"
        self.login_button_name = "button[data-selen*='login-submit']"
        self.cookie = "Button[id='cookiebotDialogOkButton']"
        self.log_button_selector = "button[data-selen*='login-submit"
        self.size_button_class = "size-selected"
        self.choose_size_selector = "span[data-selen-product-id*='3525099']"
        self.do_koszyka_class = "add-to-cart-text"
        self.zamowienie_button_selector = "a[data-selen=cart-confirmation-go-to-checkout]"
        self.kobieta_linktext = "Kobieta"
        self.dla_niej_linktext = "Dla niej"
        self.konto_button_selector = "div[data-testid*='account-info-logged-false']"
        self.wybor_sukienki_linktext = "Trapezowa sukienka"

    def open(self):
        self.driver.get('https://www.reserved.com/pl/pl/')

    def enter_username(self, username):
        field = self.driver.find_element(By.ID, self.username_field_id)
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.driver.find_element(By.ID, self.password_field_id)
        field.clear()
        field.send_keys(password)

    def click_login(self):
        button = self.driver.find_element(By.CSS_SELECTOR, self.login_button_name)
        button.click()
    
    def click_cookie(self):
        ciastko = self.driver.find_element(By.CSS_SELECTOR, self.cookie)
        ciastko.click()

    def click_log_button(self):
        log_button = self.driver.find_element(By.CSS_SELECTOR, self.log_button_selector)
        log_button.click()

    def size(self):
        size_button = self.driver.find_element(By.CLASS_NAME, self.size_button_class)
        size_button.click()

    def choose_size_button(self):
        choose_size = self.driver.find_element(By.CSS_SELECTOR, self.choose_size_selector)
        choose_size.click()

    def do_koszyka_button(self):
        do_koszyka = self.driver.find_element (By.CLASS_NAME, self.do_koszyka_class)
        do_koszyka.click()

    def zamowienie_button(self):
        zamowienie = self.driver.find_element (By.CSS_SELECTOR, self.zamowienie_button_selector)
        zamowienie.click()

    def kobieta_button(self):
        kobieta = self.driver.find_element (By.LINK_TEXT, self.kobieta_linktext)
        kobieta.click()

    def dla_niej_button(self):
        dla_niej = self.driver.find_element(By.LINK_TEXT, self.dla_niej_linktext)
        dla_niej.click()

    def konto_button(self):
        konto = self.driver.find_element (By.CSS_SELECTOR, self.konto_button_selector)
        konto.click()

    def wybor_sukienki(self):
        trapezowa_sukienka = self.driver.find_element (By.LINK_TEXT, self.wybor_sukienki_linktext)
        trapezowa_sukienka.click()