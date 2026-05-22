import allure
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.base_locators import BaseLocators

class HomePage(BasePage):

    @allure.step("Дождаться загрузки главной страницы Самоката")
    def wait_for_load_home_page(self):self.wait_for_visibility_element(HomePageLocators.order_button_up)

    @allure.step("Дождаться загрузки страницы ua.ru")
    def wait_for_load_ya_page(self):self.wait_for_visibility_element(BaseLocators.search_field)

    @allure.step("Нажать на кнопку выпадающего списка")
    def click_accordion_heading(self, locator):
        self.click_to_element(locator)

    @allure.step("Получить текст в выпадающем списке")
    def get_accordion_panel_text(self, locator):
        return self.get_text_from_element(locator)
    
    @allure.step("Проскроллить страницу до выпадающего списка")
    def scroll_to_accordion(self):
        self.scroll_to_element(HomePageLocators.accordion_heading_mkad)

    @allure.step('Кликнуть по верхней кнопку "Заказать"')
    def click_order_button_up(self):
        self.click_to_element(HomePageLocators.order_button_up)

    @allure.step('Кликнуть по нижней кнопку "Заказать"')
    def click_order_button_down(self):
        self.click_to_element(HomePageLocators.order_button_down)

    @allure.step('Кликнуть по логотипу Яндекса')
    def logo_yandex_click(self):
        self.click_to_element(BaseLocators.logo_yandex)

    @allure.step('Проверить загрузку страницы ya.ru')
    def check_redirect_ya_ru(self):
        return self.find_element(BaseLocators.search_field).is_enabled()

    @allure.step('Проверить загрузку главной страницы Самоката')
    def check_header_home_page(self):
        return self.find_element(HomePageLocators.header_home_page).is_enabled()