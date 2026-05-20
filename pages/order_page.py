from locators.order_page_locators import OrderPageLocators
from locators.base_locators import BaseLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_first_order_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.name_field))

    def wait_for_load_second_order_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.date_field))

    def set_name(self, name):
        self.driver.find_element(*OrderPageLocators.name_field).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.surname_field).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.address_field).send_keys(address)

    def metro_field_click(self):
        self.driver.find_element(*OrderPageLocators.metro_field).click()
    
    def metro_field_first_station_click(self):
        self.driver.find_element(*OrderPageLocators.metro_field_first_station).click()

    def set_phone(self, phone):
        self.driver.find_element(*OrderPageLocators.phone_field).send_keys(phone)

    def order_next_button_click(self):
        self.driver.find_element(*OrderPageLocators.order_next_button).click()

    def date_field_click(self):
        self.driver.find_element(*OrderPageLocators.date_field).click()

    def select_date_click(self):
        self.driver.find_element(*OrderPageLocators.select_date).click()

    def rental_period_field_click(self):
        self.driver.find_element(*OrderPageLocators.rental_period_field).click()

    def one_day_button_click(self):
        self.driver.find_element(*OrderPageLocators.one_day_button).click()

    def order_button_click(self):
        self.driver.find_element(*OrderPageLocators.order_button).click()

    def confirm_order_button_click(self):
        self.driver.find_element(*OrderPageLocators.confirm_order_button).click()
    
    def wait_for_load_track_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.order_placed))
    
    def text_order_placed(self):
        return self.driver.find_element(*OrderPageLocators.order_placed).text

    def fill_first_order_page(self, name, surname, address, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.metro_field_click()
        self.metro_field_first_station_click()
        self.set_phone(phone)
        self.order_next_button_click()

    def fill_second_order_page(self):
        self.date_field_click()
        self.select_date_click()
        self.rental_period_field_click()
        self.one_day_button_click()
        self.order_button_click()
        self.confirm_order_button_click()
        self.wait_for_load_track_page()

    def logo_scooter_click(self):
        self.driver.find_element(*BaseLocators.logo_scooter).click()

    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.cancel_order_button))
