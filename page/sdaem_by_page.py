from selenium.webdriver.common.by import By

from page.base_page import BasePage
import json

class SdaemByLocators:
    CITY_BUTTON = (By.ID, "city_input")
    ROOM_AMOUNT = (By.ID, "room_input_innerText")
    PRICE_PER_DAY_MIN = (By.XPATH, "//input[@placeholder='От']")
    PRICE_PER_DAY_MAX = (By.XPATH, "//input[@placeholder='До']")
    SHOW_BUTTON = (By.ID, "show_button_innerText")
    FROM_DATE = (By.ID, "start_date")
    TILL_DATE = (By.ID, "end_date")
    MORE_OPTIONS_TAB = (By.ID, "more_button_innerText")
    RENT_TYPES_CARDS_BLOCK = (By.XPATH, "//div[@class='rentTypesCardsBlock_cards']")
    RENT_TYPES_CARDS_BLOCK_BUTTON_LIST = (By.XPATH, "//div[@class='rentTypesCardsBlock_buttonList']")
    SERVICE_PRICE_BUTTON = (By.ID, "services_price_button_innerText")

class SdaemByPage(BasePage):
    def select_city(self, city: str) -> None:
        city_selector = (By.XPATH, f"//li[text()='{city}']")
        minsk_city_dropdown = self.find_element(city_selector)
        minsk_city_dropdown.click()

    def select_number_of_rooms(self, room: str) -> None:
        room_amount_dropdown = (By.XPATH, f"//li[text()='{room}']")
        room_amount = self.find_element(SdaemByLocators.ROOM_AMOUNT)
        room_amount.click()
        one_room_dropdown = self.find_element(room_amount_dropdown)
        one_room_dropdown.click()

    def select_price(self, from_price: str, to_price: str):
        price_per_day_min = self.find_element(SdaemByLocators.PRICE_PER_DAY_MIN)
        price_per_day_min.send_keys(from_price)
        price_per_day_max = self.find_element(SdaemByLocators.PRICE_PER_DAY_MAX)
        price_per_day_max.send_keys(to_price)

    def click_show_button(self):
        show_button = self.find_element(SdaemByLocators.SHOW_BUTTON)
        show_button.click()

    def open_more_options_tab(self):
        more_options_tab = self.find_element(SdaemByLocators.MORE_OPTIONS_TAB)
        more_options_tab.click()

    def select_date(self, fr: str, till: str):
        from_date = self.find_element(SdaemByLocators.FROM_DATE)
        from_date.send_keys(fr)
        till_date = self.find_element(SdaemByLocators.TILL_DATE)
        till_date.send_keys(till)

    def check_alert_field(self, alert_field, expected_alert_value):
        alert = self.driver.switch_to.alert
        json_alert = json.loads(alert.text)
        assert json_alert[alert_field] == expected_alert_value


    def alert_confirm(self):
        self.driver.switch_to.alert.accept()

    def check_rent_types_cards_block_cards(self):
        rent_types_cards_block_cards = self.find_element(SdaemByLocators.RENT_TYPES_CARDS_BLOCK)
        assert rent_types_cards_block_cards.is_displayed(), "Rent type cards are not present on the page"

    def check_rent_types_cards_block_cards_button_list(self):
        check_rent_types_cards_block_cards_button_list = self.find_element(SdaemByLocators.RENT_TYPES_CARDS_BLOCK_BUTTON_LIST)
        check_rent_types_cards_block_cards_button_list.get_attribute('rentTypesCardsBlock_buttonList'), "Rent type cards button list is not present on the page"

    def check_service_price_button(self):
        check_service_price_button = self.find_element(SdaemByLocators.SERVICE_PRICE_BUTTON)
        check_service_price_button.get_attribute('services_price_button_innerText'), "Service_price_button is not present on the page"