import allure
from pages.order_page import OrderPage
from pages.home_page import HomePage
from data.urls_data import home_page_url
from data.urls_data import track_page_url

class TestRedirects:
     
    @allure.title("Переход по логотипу Самоката")
    def test_redirect_scooter(self, driver):
        driver.get(track_page_url)
        order_page = OrderPage(driver)
        home_page = HomePage(driver)
        order_page.wait_for_load_order_page()
        order_page.logo_scooter_click()

        assert home_page.check_header_home_page()

    @allure.title("Переход по логотипу Яндекса")
    def test_redirect_yandex(self, driver): 
        driver.get(home_page_url)
        home_page = HomePage(driver)
        home_page.wait_for_load_home_page()
        home_page.logo_yandex_click()
        home_page.switch_to_new_window()
        home_page.wait_for_load_ya_page()
        assert home_page.check_redirect_ya_ru()
        
