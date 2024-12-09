import pytest
import allure
from locators.locators import Locators
from pages.base_page import BasePage
from src.config import SEARCH_URL, BASE_URL


@pytest.mark.usefixtures("driver")
class TestMainFunctionality:
    @allure.title("Открытие и поиск по запросу.")
    def test_search_request(self, driver):
        driver.get(SEARCH_URL)
        page = BasePage(driver)

        page.click_element_search_url()
        page.enter_search_input("Onliner")
        page.click_search_button()

        assert "Onliner" in driver.page_source

    @allure.title("Открытие главной страницы")
    def test_open_link(self, driver):
        driver.get(SEARCH_URL)
        page = BasePage(driver)

        page.click_element_search_url()
        page.enter_search_input("Onliner")
        page.click_search_button()
        page.click_search_field()

        assert BASE_URL in driver.current_url

    @allure.title("Успешная авторизация")
    def test_login(self, driver):
        driver.get(SEARCH_URL)
        page = BasePage(driver)

        page.click_element_search_url()
        page.enter_search_input("Onliner")
        page.click_search_button()
        page.click_search_field()
        page.click_login_button()
        page.enter_email_input("cokol2122@mail.ru")
        page.enter_password_input("test_password")
        page.click_submit_button()

        assert driver.find_element(*Locators.CHAT_BUTTON).is_displayed()

    @allure.title("Проверка категории Мобильные телефоны.")
    def test_phone_field_true(self, driver):
        driver.get(SEARCH_URL)
        page = BasePage(driver)

        page.click_element_search_url()
        page.enter_search_input("Onliner")
        page.click_search_button()
        page.click_search_field()
        page.click_login_button()
        page.enter_email_input("cokol2122@mail.ru")
        page.enter_password_input("test_password")
        page.click_submit_button()
        page.click_phone_button()

        assert driver.find_element(*Locators.PHONE_FIELD).is_displayed()

    @allure.title("Проверика, что имееется ссылка для сравнения и наличие флажков.")
    def test_add_phone_check_link(self, driver):
        driver.get(SEARCH_URL)
        page = BasePage(driver)
        page.click_phone_button()
        page.click_checkbox_item()
        page.scroll_click_checkbox_item()
        page.click_checkbox_item()
        page.click_checkbox_by_index(0)
        page.click_checkbox_by_index(1)

        checkboxes = driver.find_elements(*Locators.COMPARE_CHECKBOX)
        for checkbox in checkboxes:
            assert checkbox.is_selected()

    @allure.title("Проверка выбранных телефонов и наличие флажков.")
    def test_size_screen_and_price(self, driver):
        driver.get(SEARCH_URL)
        page = BasePage(driver)
        page.click_phone_button()
        page.click_checkbox_item()
        page.scroll_click_checkbox_item()
        page.click_checkbox_item()
        page.click_checkbox_by_index(0)
        page.click_checkbox_by_index(1)
        page.enter_min_price("1")
        page.enter_max_price("9999")
        page.click_select_min_screen()
        page.click_select_min_screen()

        assert driver.find_element(*Locators.COMPARE_BUTTON).is_displayed()
        assert driver.find_element(*Locators.COMPARE_CHECKBOX_CHECK).is_displayed()

    @allure.title("Проверка, совпадения параметров с предыдущей страницей ")
    def test_size_price_ram_os(self, driver):
        driver.get(SEARCH_URL)
        page = BasePage(driver)
        page.click_phone_button()
        page.click_checkbox_item()
        page.scroll_click_checkbox_item()
        page.click_checkbox_item()
        page.click_checkbox_by_index(0)
        page.click_checkbox_by_index(1)
        page.enter_min_price("1")
        page.enter_max_price("9999")
        page.click_select_min_screen()
        page.click_select_min_screen()
        page.click_first_item()

        element_1 = driver.find_element(*Locators.OPTIONS_PHONE_1)
        element_2 = driver.find_element(*Locators.OPTIONS_PHONE_2)
        element_3 = driver.find_element(*Locators.OPTIONS_PHONE_3)
        element_4 = driver.find_element(*Locators.OPTIONS_PHONE_4)
        elements_all = driver.find_elements(*Locators.ALL_OPTIONS_PHONE)

        assert element_1 in elements_all
        assert element_2 in elements_all
        assert element_3 in elements_all
        assert element_4 in elements_all

    @allure.title("Проверка, что два телефона содержат правильную информацию ")
    def test_collation_items(self, driver):
        driver.get(SEARCH_URL)
        page = BasePage(driver)
        page.click_phone_button()
        page.click_checkbox_item()
        page.scroll_click_checkbox_item()
        page.click_checkbox_item()
        page.click_checkbox_by_index(0)
        page.click_checkbox_by_index(1)
        page.enter_min_price("1")
        page.enter_max_price("9999")
        page.click_select_min_screen()
        page.click_select_min_screen()
        page.click_collation_button()

        element_1 = driver.find_element(*Locators.Locators.NAME_ITEM_1)
        element_2 = driver.find_element(*Locators.Locators.NAME_ITEM_2)
        assert element_1 != element_2

    @allure.title("Проверка наличие добавленного товара в корзине")
    def test_add_items_basket(self, driver):
        driver.get(SEARCH_URL)
        page = BasePage(driver)
        page.click_phone_button()
        page.click_checkbox_item()
        page.scroll_click_checkbox_item()
        page.click_checkbox_item()
        page.click_checkbox_by_index(0)
        page.click_checkbox_by_index(1)
        page.enter_min_price("1")
        page.enter_max_price("9999")
        page.click_select_min_screen()
        page.click_select_min_screen()
        page.click_collation_button()
        page.click_first_item()
        page.add_item_basket()

        assert driver.find_element(*Locators.SUCCESSFUL_MESSAGE).is_displayed()
