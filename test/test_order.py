import allure
import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage
from data.order_data import OrderData
from data.urls_data import home_page_url

class TestOrder:

    @allure.title("Позитивный сценарий оформления заказа")
    @pytest.mark.parametrize("button_type, name, surname, address, phone", OrderData.DATA_SET)

    def test_scooter_order_flow(self, driver, button_type, name, surname, address, phone):
        driver.get(home_page_url)
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        
        home_page.wait_for_load_home_page()
        
        button_actions = {
            "up": home_page.click_order_button_up,
            "down": lambda: (
                home_page.scroll_to_accordion(),
                home_page.click_order_button_down()
            )
        }
        button_actions[button_type]()
            
        order_page.wait_for_load_first_order_page()
        order_page.fill_first_order_page(name, surname, address, phone)
        order_page.wait_for_load_second_order_page()
        order_page.fill_second_order_page()
        
        assert "Заказ оформлен" in order_page.text_order_placed()

