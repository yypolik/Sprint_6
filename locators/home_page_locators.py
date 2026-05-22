from selenium.webdriver.common.by import By

class HomePageLocators:
    header_home_page = [By.CSS_SELECTOR, '.Home_Header__iJKdX']
    accordion_heading_price = [By.ID, 'accordion__heading-0']
    accordion_panel_price = [By.ID, 'accordion__panel-0']
    accordion_heading_amount = [By.ID, 'accordion__heading-1']
    accordion_panel_amount = [By.ID, 'accordion__panel-1']
    accordion_heading_time = [By.ID, 'accordion__heading-2']
    accordion_panel_time = [By.ID, 'accordion__panel-2']
    accordion_heading_today = [By.ID, 'accordion__heading-3']
    accordion_panel_today = [By.ID, 'accordion__panel-3']
    accordion_heading_prolong = [By.ID, 'accordion__heading-4']
    accordion_panel_prolong = [By.ID, 'accordion__panel-4']
    accordion_heading_charger = [By.ID, 'accordion__heading-5']
    accordion_panel_charger = [By.ID, 'accordion__panel-5']
    accordion_heading_cancel = [By.ID, 'accordion__heading-6']
    accordion_panel_cancel = [By.ID, 'accordion__panel-6']
    accordion_heading_mkad = [By.ID, 'accordion__heading-7']
    accordion_panel_mkad = [By.ID, 'accordion__panel-7']

    order_button_up = [By.CSS_SELECTOR, '.Header_Nav__AGCXC .Button_Button__ra12g']
    order_button_down = [By.CSS_SELECTOR, '.Home_FinishButton__1_cWm .Button_Button__ra12g']

