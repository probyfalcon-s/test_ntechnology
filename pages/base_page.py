from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from conftest import driver
from locators.locators import Locators
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_click(self, locator, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    def wait_and_send_keys(self, locator, text, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def wait_element(self, locator, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element_search_url(self):
        self.wait_and_click(Locators.SEARCH_INPUT)

    def enter_search_input(self, text):
        self.wait_and_send_keys(Locators.SEARCH_INPUT, text)

    def click_search_button(self):
        self.wait_and_click(Locators.SEARCH_BUTTON)

    def click_search_field(self):
        self.wait_and_click(Locators.SEARCH_FIELD)

    def click_login_button(self):
        self.wait_and_click(Locators.LOGIN_BUTTON)

    def enter_email_input(self, text):
        self.wait_and_send_keys(Locators.EMAIL_INPUT, text)

    def enter_password_input(self, text):
        self.wait_and_send_keys(Locators.PASSWORD_INPUT, text)

    def click_submit_button(self):
        self.wait_and_click(Locators.SUBMIT_BUTTON)

    def click_phone_button(self):
        self.wait_and_click(Locators.PHONE_BUTTON)

    def click_checkbox_item(self):
        self.wait_and_click(Locators.COMPARE_CHECKBOX)

    def click_checkbox_by_index(self, index):
        elements = self.driver.find_elements(*Locators.COMPARE_CHECKBOX)

        element = elements[index]
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def enter_min_price(self, text):
        self.wait_and_send_keys(Locators.MIN_PRICE_INPUT, text)

    def enter_max_price(self, text):
        self.wait_and_send_keys(Locators.MAX_PRICE_INPUT, text)

    def click_select_min_screen(self):
        select_element = driver.find_element(*Locators.MIN_SCREEN_SELECT)
        dropdown = Select(select_element)
        dropdown.select_by_visible_text("")
        dropdown.select_by_value("68x68")
        dropdown.select_by_index(1)

    def click_select_max_screen(self):
        select_element = driver.find_element(*Locators.MAX_SCREEN_SELECT)
        dropdown = Select(select_element)
        dropdown.select_by_visible_text("")
        dropdown.select_by_value("2496x2224")
        dropdown.select_by_index(1)

    def click_first_item(self):
        self.wait_and_click(Locators.FIRST_ITEM)

    def click_collation_button(self):
        self.wait_and_click(Locators.COMPARE_BUTTON)

    def click_first_item(self):
        self.wait_and_click(Locators.NAME_ITEM_1)

    def add_item_basket(self):
        self.wait_and_click(Locators.ADD_ITEM_BASKET)






