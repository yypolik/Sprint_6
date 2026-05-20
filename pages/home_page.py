from locators.home_page_locators import HomePageLocators
from locators.base_locators import BaseLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.order_button_up))

    def wait_for_load_ya_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(BaseLocators.search_field))

    def click_accordion_heading_price(self):
        self.driver.find_element(*HomePageLocators.accordion_heading_price).click()
    
    def get_text_accordion_panel_price(self):
       return self.driver.find_element(*HomePageLocators.accordion_panel_price).text


    def click_accordion_heading_amount(self):
        self.driver.find_element(*HomePageLocators.accordion_heading_amount).click()

    def get_text_accordion_panel_amount(self):
        return self.driver.find_element(*HomePageLocators.accordion_panel_amount).text


    def click_accordion_heading_time(self):
        self.driver.find_element(*HomePageLocators.accordion_heading_time).click()

    def get_text_accordion_panel_time(self):
        return self.driver.find_element(*HomePageLocators.accordion_panel_time).text


    def click_accordion_heading_today(self):
        self.driver.find_element(*HomePageLocators.accordion_heading_today).click()

    def get_text_accordion_panel_today(self):
        return self.driver.find_element(*HomePageLocators.accordion_panel_today).text


    def click_accordion_heading_prolong(self):
        self.driver.find_element(*HomePageLocators.accordion_heading_prolong).click()

    def get_text_accordion_panel_prolong(self):
        return self.driver.find_element(*HomePageLocators.accordion_panel_prolong).text


    def click_accordion_heading_charger(self):
        self.driver.find_element(*HomePageLocators.accordion_heading_charger).click()

    def get_text_accordion_panel_charger(self):
        return self.driver.find_element(*HomePageLocators.accordion_panel_charger).text


    def click_accordion_heading_cancel(self):
        self.driver.find_element(*HomePageLocators.accordion_heading_cancel).click()

    def get_text_accordion_panel_cancel(self):
        return self.driver.find_element(*HomePageLocators.accordion_panel_cancel).text


    def click_accordion_heading_mkad(self):
        self.driver.find_element(*HomePageLocators.accordion_heading_mkad).click()

    def get_text_accordion_panel_mkad(self):
        return self.driver.find_element(*HomePageLocators.accordion_panel_mkad).text
    
    def scroll_to_accordion(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*HomePageLocators.accordion_heading_mkad)) 

    def click_order_button_up(self):
        self.driver.find_element(*HomePageLocators.order_button_up).click()

    def click_order_button_down(self):
        self.driver.find_element(*HomePageLocators.order_button_down).click()

    def logo_yandex_click(self):
        self.driver.find_element(*BaseLocators.logo_yandex).click()

    def check_redirect_ya_ru(self):
        return self.driver.find_element(*BaseLocators.search_field).is_enabled()
    
    def check_header_home_page(self):
        return self.driver.find_element(*HomePageLocators.header_home_page).is_enabled()