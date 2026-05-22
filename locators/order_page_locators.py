from selenium.webdriver.common.by import By

class OrderPageLocators:    
    name_field = [By.CSS_SELECTOR, '.Order_Form__17u6u [class^="Input"]:nth-child(1) input']
    surname_field = [By.CSS_SELECTOR, '.Order_Form__17u6u [class^="Input"]:nth-child(2) input']
    address_field = [By.CSS_SELECTOR, '.Order_Form__17u6u [class^="Input"]:nth-child(3) input']
    metro_field = [By.CSS_SELECTOR, '.select-search__input']
    metro_field_first_station = [By.CSS_SELECTOR, '.select-search__row:nth-child(1) button']
    phone_field = [By.CSS_SELECTOR, '.Order_Form__17u6u [class^="Input"]:nth-child(5) input']
    order_next_button = [By.CSS_SELECTOR, '.Order_NextButton__1_rCA button']
    date_field = [By.CSS_SELECTOR, '.react-datepicker-wrapper .Input_Input__1iN_Z']
    select_date = [By.CSS_SELECTOR, '.react-datepicker__week:last-child :last-child']
    rental_period_field = [By.CSS_SELECTOR, '.Dropdown-placeholder']
    one_day_button = [By.CSS_SELECTOR, '.Dropdown-menu :first-child']
    order_button = [By.CSS_SELECTOR, '.Order_Buttons__1xGrp :last-child']
    confirm_order_button = [By.CSS_SELECTOR, '.Order_Modal__YZ-d3 .Order_Buttons__1xGrp :last-child']
    order_placed = [By.CSS_SELECTOR, '.Order_ModalHeader__3FDaJ']
    cancel_order_button = [By.CSS_SELECTOR, '.Track_OrderColumns__2r_1F button']
