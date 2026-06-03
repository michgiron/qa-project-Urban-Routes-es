from time import sleep
from typing import Self

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v147.debugger import pause
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_cap = (By.XPATH,"//button[text()='Pedir un taxi']")
    select_comfort = (By.XPATH,"//div[@class='tcard-title' and text ()= 'Comfort']")
    comfort_selected = (By.XPATH, "//div[contains(@class, 'tcard') and contains(., 'Comfort')]")
    add_phone = (By.XPATH, "//div[@class='np-text' and text()='Número de teléfono']")
    input_text_phone = (By.XPATH, "//input[@id='phone']")
    sel_next = (By.XPATH, "//button[@class='button full' and text()='Siguiente']")
    input_phone_code = (By.XPATH, "//div[contains(@class,'input-container') and not(contains(@class,'hidden'))]//input[@id='code']")
    sel_confirm = (By.XPATH, "//button[text()='Confirmar']")
    phone_number_added = (By.CSS_SELECTOR, "div.np-text")
    sel_pay= (By.XPATH, "//div[@class='pp-text']")
    sel_debit= (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    input_debit = (By.XPATH, "//input[@id='number']")
    input_code = (By.XPATH, "//input[@name='code']")
    sel_add_debit = (By.XPATH, "//button[@class='button full' and text()='Agregar']")
    cl_debit_card = (By.XPATH, "//div[@class='payment-picker open']//div[@class='section active']//button[@class='close-button section-close']")
    message_driver = (By.XPATH, "//input[@id='comment']")
    req_order = (By.XPATH, "//div[@class='reqs-head']")
    req_tissue = (By.XPATH, "//div[normalize-space()='Manta y pañuelos']/following-sibling::div//span[@class='slider round']")
    check_tissue = (By.CSS_SELECTOR, "input.switch-input")
    req_ice_cream = (By.XPATH, "//div[normalize-space()='Helado']/following-sibling::div//div[@class='counter-plus']")
    ice_cream_quantity_added = (By.CSS_SELECTOR, "div.counter-value")
    request_taxi_button_cap= (By.XPATH, "//span[@class='smart-button-secondary']")
    driver_wait_time = (By.XPATH, "//div[contains(@class,'order-header-title')]")

    def __init__(self, driver : WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_from(self, from_address):
        self.wait.until(EC.visibility_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(EC.visibility_of_element_located(self.to_field)).send_keys(to_address)

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_from(self):
        return self.wait.until(EC.visibility_of_element_located(self.from_field)).get_property('value')

    def get_to(self):
        return self.wait.until(EC.visibility_of_element_located(self.to_field)).get_property('value')

    def click_req_cap(self):
        self.wait.until(EC.element_to_be_clickable(self.request_cap)).click()

    def is_enabled_req_cap(self):
        return self.wait.until(EC.element_to_be_clickable(self.request_cap)).is_enabled()

    def click_select_comfort(self):
        self.wait.until(EC.element_to_be_clickable(self.select_comfort)).click()

    def is_enabled_select_comfort(self):
        return self.wait.until(EC.element_to_be_clickable(self.select_comfort)).is_enabled()

    def is_selected_comfort(self):
        return self.wait.until(EC.element_to_be_clickable(self.comfort_selected)).get_attribute("class")

    def click_add_phone(self):
        self.wait.until(EC.element_to_be_clickable(self.add_phone)).click()

    def is_enabled_add_phone(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_phone)).is_enabled()

    def set_phone(self, phone_number):
        self.wait.until(EC.visibility_of_element_located(self.input_text_phone)).send_keys(phone_number)

    def get_phone(self):
        #return self.wait.until(EC.visibility_of_element_located(self.from_field)).get_property('value')
        return self.wait.until(EC.visibility_of_element_located(self.input_text_phone)).get_property('value')

    def is_enabled_sel_next(self):
        return self.wait.until(EC.element_to_be_clickable(self.sel_next)).is_enabled()

    def click_sel_next(self):
        self.wait.until(EC.element_to_be_clickable(self.sel_next)).click()

    def set_phone_code(self, phone_code):
        self.wait.until(EC.visibility_of_element_located(self.input_phone_code)).send_keys(phone_code)

    def get_phone_code(self):
        return self.wait.until(EC.element_to_be_clickable(self.input_phone_code)).get_property('value')

    def is_enabled_conf_phone(self):
        return self.wait.until(EC.element_to_be_clickable(self.sel_confirm)).is_enabled()

    def click_conf_phone(self):
        self.wait.until(EC.element_to_be_clickable(self.sel_confirm)).click()

    def get_phone_number_added(self):
        return self.wait.until(EC.visibility_of_element_located(self.phone_number_added)).text

    def click_payment_method(self):
        self.wait.until(EC.element_to_be_clickable(self.sel_pay)).click()

    def is_enabled_payment_method(self):
        return self.wait.until(EC.element_to_be_clickable(self.sel_pay)).is_enabled()

    def click_select_debit(self):
        self.wait.until(EC.visibility_of_element_located(self.sel_debit)).click()

    def is_enabled_select_debit(self):
        return self.wait.until(EC.element_to_be_clickable(self.sel_debit)).is_enabled()

    def set_debit_number(self, debit_number):
        self.wait.until(EC.visibility_of_element_located(self.input_debit)).send_keys(debit_number)

    def get_debit_number(self):
        return self.wait.until(EC.visibility_of_element_located(self.input_debit)).get_property('value')

    def set_code(self, code_number):
        element = self.wait.until(EC.visibility_of_element_located(self.input_code))
        element.send_keys(code_number)
        element.send_keys(Keys.TAB)

    def get_code(self):
        return self.wait.until(EC.visibility_of_element_located(self.input_code)).get_property('value')

    def is_enabled_sel_add_debit(self):
        return self.wait.until(EC.element_to_be_clickable(self.sel_add_debit)).is_enabled()

    def click_sel_add_debit(self):
        self.wait.until(EC.element_to_be_clickable(self.sel_add_debit)).click()

    def is_enabled_cl_debit_card(self):
        return self.wait.until(EC.visibility_of_element_located(self.cl_debit_card)).is_enabled()

    def click_cl_debit_card(self):
        self.wait.until(EC.visibility_of_element_located(self.cl_debit_card)).click()

    def is_enabled_mns_driver(self):
        return self.wait.until(EC.element_to_be_clickable(self.message_driver)).is_enabled()

    def click_mns_driver(self):
        element = self.wait.until(
            EC.presence_of_element_located(self.message_driver)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def set_mns_driver(self, message):
        self.wait.until(EC.visibility_of_element_located(self.message_driver)).send_keys(message)

    def get_mns_driver(self):
        return self.wait.until(EC.visibility_of_element_located(self.message_driver)).get_property('value')

    def is_enabled_require_order(self):
        return self.wait.until(EC.element_to_be_clickable(self.req_order)).is_enabled()

    def click_require_order(self):
        self.wait.until(EC.element_to_be_clickable(self.req_order)).click()

    def is_enabled_blanket_tissue(self):
        return self.wait.until(EC.element_to_be_clickable(self.req_tissue)).is_enabled()

    def click_blanket_tissue(self):
        self.wait.until(EC.element_to_be_clickable(self.req_tissue)).click()

    def is_checked_blanket_tissue(self):
        return self.wait.until(EC.presence_of_element_located(self.check_tissue)).is_selected()

    def is_enabled_ice_cream(self):
        return self.wait.until(EC.element_to_be_clickable(self.req_ice_cream)).is_enabled()

    def add_ice_cream(self, ice_cream_quantity):
        for i in range(ice_cream_quantity):
            self.wait.until(EC.element_to_be_clickable(self.req_ice_cream)).click()
            sleep(0.5)

    def get_ice_cream_quantity_added(self):
        return self.wait.until(EC.visibility_of_element_located(self.ice_cream_quantity_added)).text

    def is_enabled_request_taxi(self):
        return self.wait.until(EC.element_to_be_clickable(self.request_taxi_button_cap)).is_enabled()

    def click_request_taxi_cap(self):
        self.wait.until(EC.element_to_be_clickable(self.request_taxi_button_cap)).click()

    def wait_driver_assigned(self):
        self.wait.until(EC.visibility_of_element_located(self.driver_wait_time))