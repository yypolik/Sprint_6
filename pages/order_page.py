import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.base_locators import BaseLocators


class OrderPage(BasePage):

    @allure.step("Дождаться загрузки первой страницы формы заказа")
    def wait_for_load_first_order_page(self):
        self.wait_for_visibility_element(OrderPageLocators.name_field)

    @allure.step("Дождаться загрузки второй страницы формы заказа")
    def wait_for_load_second_order_page(self):
        self.wait_for_visibility_element(OrderPageLocators.date_field)

    @allure.step("Ввести имя")
    def set_name(self, name):
        self.set_text_to_element(OrderPageLocators.name_field, name)

    @allure.step("Ввести фамилию")
    def set_surname(self, surname):
        self.set_text_to_element(OrderPageLocators.surname_field, surname)

    @allure.step("Ввести адрес")
    def set_address(self, address):
        self.set_text_to_element(OrderPageLocators.address_field, address)

    @allure.step("Кликнуть на поле Станция метро")
    def metro_field_click(self):
        self.click_to_element(OrderPageLocators.metro_field)

    @allure.step("Выбрать станцию метро")
    def metro_field_first_station_click(self):
        self.click_to_element(OrderPageLocators.metro_field_first_station)

    @allure.step("Ввести номер телефона")
    def set_phone(self, phone):
        self.set_text_to_element(OrderPageLocators.phone_field, phone)

    @allure.step('Кликнуть на кнопку "Далее"')
    def order_next_button_click(self):
        self.click_to_element(OrderPageLocators.order_next_button)

    @allure.step("Кликнуть на поле Дата")
    def date_field_click(self):
        self.click_to_element(OrderPageLocators.date_field)

    @allure.step("Выбрать дату")
    def select_date_click(self):
        self.click_to_element(OrderPageLocators.select_date)

    @allure.step("Кликнуть на поле Срок аренды")
    def rental_period_field_click(self):
        self.click_to_element(OrderPageLocators.rental_period_field)

    @allure.step("Выбрать срок 1 день")
    def one_day_button_click(self):
        self.click_to_element(OrderPageLocators.one_day_button)

    @allure.step('Кликнуть на кнопку "Заказать"') 
    def order_button_click(self):
        self.click_to_element(OrderPageLocators.order_button)

    @allure.step('Кликнуть на кнопку "Да"') 
    def confirm_order_button_click(self):
        self.click_to_element(OrderPageLocators.confirm_order_button)

    @allure.step('Дождаться загрузки окна с трек-номером') 
    def wait_for_load_track_page(self):
        self.wait_for_visibility_element(OrderPageLocators.order_placed)

    @allure.step('Получить текст окна с трек-номером') 
    def text_order_placed(self):
        return self.get_text_from_element(OrderPageLocators.order_placed)

    @allure.step('Заполнить первую страницу формы заказа') 
    def fill_first_order_page(self, name, surname, address, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.metro_field_click()
        self.metro_field_first_station_click()
        self.set_phone(phone)
        self.order_next_button_click()

    @allure.step('Заполнить вторую страницу формы заказа') 
    def fill_second_order_page(self):
        self.date_field_click()
        self.select_date_click()
        self.rental_period_field_click()
        self.one_day_button_click()
        self.order_button_click()
        self.confirm_order_button_click()
        self.wait_for_load_track_page()

    @allure.step('Кликнуть по логотипу Самоката') 
    def logo_scooter_click(self):
        self.click_to_element(BaseLocators.logo_scooter)

    @allure.step('Дождаться загрузки окна заказа') 
    def wait_for_load_order_page(self):
        self.wait_for_visibility_element(OrderPageLocators.cancel_order_button)