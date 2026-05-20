from selenium import webdriver
from pages.order_page import OrderPage
from pages.home_page import HomePage

class TestRedirects:

    driver = None
    
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        
    def test_redirect_scooter(self):
        self.driver.get("https://qa-scooter.education-services.ru/track?t=949832")
        order_page = OrderPage(self.driver)
        home_page = HomePage(self.driver)
        order_page.wait_for_load_order_page()
        order_page.logo_scooter_click()

        assert home_page.check_header_home_page()

    def test_redirect_yandex(self): 
        self.driver.get("https://qa-scooter.education-services.ru/")
        home_page = HomePage(self.driver)
        home_page.wait_for_load_home_page()
        home_page.logo_yandex_click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        home_page.wait_for_load_ya_page()
        assert home_page.check_redirect_ya_ru()
        
    @classmethod
    def teardown_class(cls):
        cls.driver.quit() 