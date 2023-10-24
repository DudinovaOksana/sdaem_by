from page.sdaem_by_page import SdaemByPage


class TestSdaemBy:

    def test_tab_apartments_per_day(self, driver):
        city = "Минск"
        n_rooms = "1 комната"
        from_price = "1000"
        to_price = "40000"

        sdaem_by_page = SdaemByPage(driver, 'https://kamrad33.github.io/index.html')
        sdaem_by_page.go_to_site()

        sdaem_by_page = SdaemByPage(driver)
        sdaem_by_page.select_city(city)
        sdaem_by_page.select_number_of_rooms(n_rooms)
        sdaem_by_page.select_price(from_price, to_price)
        sdaem_by_page.click_show_button()
        sdaem_by_page.check_alert_field("city", city)
        sdaem_by_page.check_alert_field("room", n_rooms)
        sdaem_by_page.check_alert_field("priceFrom", from_price)
        sdaem_by_page.check_alert_field("priceTo", to_price)
        sdaem_by_page.alert_confirm()

    def test_tab_apartments_per_day_more_options(self, driver):
        city = "Минск"
        n_rooms = "1 комната"
        from_price = "1000"
        to_price = "40000"
        from_date = "12122023"
        till_date = "19122023"

        sdaem_by_page = SdaemByPage(driver, 'https://kamrad33.github.io/index.html')
        sdaem_by_page.go_to_site()
        sdaem_by_page = SdaemByPage(driver)
        sdaem_by_page.select_city(city)
        sdaem_by_page.select_number_of_rooms(n_rooms)
        sdaem_by_page.select_price(from_price, to_price)
        sdaem_by_page.open_more_options_tab()
        sdaem_by_page.select_date(from_date, till_date)
        sdaem_by_page.click_show_button()
        sdaem_by_page.check_alert_field("city", city)
        sdaem_by_page.check_alert_field("room", n_rooms)
        sdaem_by_page.check_alert_field("priceFrom", from_price)
        sdaem_by_page.check_alert_field("priceTo", to_price)
        sdaem_by_page.alert_confirm()

    def test_rent_types_cards_block_cards_and_its_list(self, driver):
        sdaem_by_page = SdaemByPage(driver, 'https://kamrad33.github.io/index.html')
        sdaem_by_page.go_to_site()
        sdaem_by_page = SdaemByPage(driver)
        sdaem_by_page.check_rent_types_cards_block_cards()

