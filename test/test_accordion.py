from selenium import webdriver
from pages.home_page import HomePage
from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestAccordion:

    driver = None
    
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://qa-scooter.education-services.ru/")
        home_page = HomePage(cls.driver)
        home_page.wait_for_load_home_page()
        home_page.scroll_to_accordion()

    def test_accordion_panel_price(self):
        
        home_page = HomePage(self.driver)
        home_page.click_accordion_heading_price()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.accordion_panel_price))
        assert home_page.get_text_accordion_panel_price() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    def test_accordion_panel_amount(self):
        
        home_page = HomePage(self.driver)
        home_page.click_accordion_heading_amount()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.accordion_panel_amount))
        assert home_page.get_text_accordion_panel_amount() == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    def test_accordion_panel_time(self):
        
        home_page = HomePage(self.driver)
        home_page.click_accordion_heading_time()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.accordion_panel_time))
        assert home_page.get_text_accordion_panel_time() == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
   
    def test_accordion_panel_today(self):
        
        home_page = HomePage(self.driver)
        home_page.click_accordion_heading_today()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.accordion_panel_today))
        assert home_page.get_text_accordion_panel_today() == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    def test_accordion_panel_prolong(self):
        
        home_page = HomePage(self.driver)
        home_page.click_accordion_heading_prolong()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.accordion_panel_prolong))
        assert home_page.get_text_accordion_panel_prolong() == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
   
    def test_accordion_panel_charger(self):
        
        home_page = HomePage(self.driver)
        home_page.click_accordion_heading_charger()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.accordion_panel_charger))
        assert home_page.get_text_accordion_panel_charger() == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    def test_accordion_panel_cancel(self):
        
        home_page = HomePage(self.driver)
        home_page.click_accordion_heading_cancel()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.accordion_panel_cancel))
        assert home_page.get_text_accordion_panel_cancel() == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    def test_accordion_panel_mkad(self):
        
        home_page = HomePage(self.driver)
        home_page.click_accordion_heading_mkad()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.accordion_panel_mkad))
        assert home_page.get_text_accordion_panel_mkad() == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    
    @classmethod
    def teardown_class(cls):
        cls.driver.quit() 