import allure
import pytest
from pages.home_page import HomePage
from data.urls_data import home_page_url
from data.accordion_data import AccordionData
from locators.home_page_locators import HomePageLocators


class TestAccordion:

    @allure.title("Проверка текста в accordion")
    @pytest.mark.parametrize("heading, panel, expected_text",AccordionData.ACCORDION_DATA)

    def test_accordion(self, driver, heading, panel, expected_text):

        driver.get(home_page_url)
        home_page = HomePage(driver)
        home_page.wait_for_load_home_page()
        home_page.scroll_to_accordion()

        heading_locator = getattr(HomePageLocators,heading)
        panel_locator = getattr(HomePageLocators,panel)

        home_page.click_accordion_heading(heading_locator)
        home_page.wait_for_visibility_element(panel_locator)

        assert home_page.get_accordion_panel_text(panel_locator) == expected_text