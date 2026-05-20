import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.order_page import OrderPage
from data.order_data import OrderData

class TestOrder:

    driver = None
    
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize("button_type, name, surname, address, phone", OrderData.DATA_SET)
    def test_scooter_order_flow(self, button_type, name, surname, address, phone):
        self.driver.get("https://qa-scooter.education-services.ru/")
        home_page = HomePage(self.driver)
        order_page = OrderPage(self.driver)
        
        home_page.wait_for_load_home_page()
        
        if button_type == "up":
            home_page.click_order_button_up()
        else:
            home_page.scroll_to_accordion() 
            home_page.click_order_button_down()
            
        order_page.wait_for_load_first_order_page()
        order_page.fill_first_order_page(name, surname, address, phone)
        order_page.wait_for_load_second_order_page()
        order_page.fill_second_order_page()
        
        assert "Заказ оформлен" in order_page.text_order_placed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit() 