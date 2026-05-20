from selenium.webdriver.common.by import By

class BaseLocators:     
    logo_yandex = [By.CSS_SELECTOR, '.Header_LogoYandex__3TSOI']
    search_field = [By.ID, 'text']
    logo_scooter = [By.CSS_SELECTOR, '.Header_LogoScooter__3lsAR']