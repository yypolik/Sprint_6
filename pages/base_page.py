from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def click_to_element(self, locator):
        self.find_element(locator).click()
    
    def set_text_to_element(self, locator, text):
        self.find_element(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element(locator).text
    
    def wait_for_visibility_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",element)

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def open_page(self, url):
        self.driver.get(url)

