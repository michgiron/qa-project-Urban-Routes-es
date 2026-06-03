import self
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import data
import helpers
from helpers import retrieve_phone_code
from data import card_number, card_code

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #SELECTORES PARA DIRECCIONES
    button_from = (By.ID, 'from')
    button_to = (By.ID, 'to')
    order_taxi = (By.CLASS_NAME, "button.round")
    laboral_button = (By.XPATH, "//div[text()='Laboral' and @class='tcard-title']")
    comfort_tariff_button = (By.XPATH, "//div[text()='Comfort' and @class='tcard-title']")

    # SELECTORES PARA NUMERO DE TELEFONO
    click_phone_number = (By.CLASS_NAME, "np-text")
    add_phone_number = (By.ID, 'phone')
    phone_full_next_button = (By.CSS_SELECTOR, 'button[type="submit"]')
    #SELECTORES PARA CODIGO SMS
    introduce_sms_code = (By.XPATH, '//*[@id="code"]')
    confirm_sms_code = (By.XPATH, "//button[text()='Confirmar']")

    #SELECTORES PARA TARJETA DE CREDITO
    payment_method = (By.CSS_SELECTOR, ".pp-button.filled")
    add_credit_card = (By.CLASS_NAME, "pp-plus")
    add_card_number = (By.XPATH, "//input[contains(@type, 'text') and contains(@id, 'number')]")
    add_code_number = (By.CLASS_NAME, 'card-input')
    card_plc_image = (By.CLASS_NAME, 'plc')
    add_full_info_card = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/form/div[3]/button[1]")
    close_method_card = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")
    confirm_credit_card_added = (By.CLASS_NAME, 'pp-value-text')

    #SELECTORES PARA MENSAJE A CONDUCTOR
    box_message_for_driver = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[3]/div/label")

    #SELECTOR PARA ORDENAR BLANKET Y HANDKERCHIEFS
    order_blanket_and_handkerchiefs = (By.XPATH, "//input[@type='checkbox']/following-sibling::span[@class='slider round']")
    # SELECTOR PARA PEDIR HELADO
    order_ice_cream_plus = (By.XPATH, "//div[contains(text(),'Helado')]//div[@class='counter-plus']")
    # SELECTOR PARA PEDIR TAXI Y DRIVER MODAL
    smart = (By.CLASS_NAME, 'smart-button-wrapper')
    driver_modal = (By.CSS_SELECTOR, ".order-body.driver-info")

    def set_route_from(self):
        button_from = WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(self.button_from))
        button_from.send_keys(data.address_from)

    def set_route_to(self):
        button_to = self.driver.find_element(*self.button_to)
        button_to.send_keys(data.address_to)

    def get_from(self):
        return self.driver.find_element(*self.button_from).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.button_to).get_property('value')

    def order_a_taxi(self):
        order_taxi = WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(self.order_taxi))
        order_taxi.click()

    # COMFORT TARIFF
    def comfort_the_tariff_button(self):
        comfort_tariff_button = WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(self.comfort_tariff_button))
        comfort_tariff_button.click()
        return comfort_tariff_button.text

    #TELEFONO

    def open_phone_number_box(self):
        click_phone_number = WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(self.click_phone_number))
        click_phone_number.click()

    def write_phone_number(self, phone_number):
        add_phone_number = WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(self.add_phone_number))
        add_phone_number.send_keys(phone_number)

    def get_phone_number(self):
        phone_number = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(self.click_phone_number))
        return phone_number.text

    def next_button(self):
        phone_full_next_button = WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(self.phone_full_next_button))
        phone_full_next_button.click()

    def fill_sms_code(self, sms_code):
        introduce_sms_code = WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.introduce_sms_code))
        introduce_sms_code.send_keys(sms_code)

    def confirm_button_sms_code(self):
        confirm_sms_code = WebDriverWait(self.driver,3).until(expected_conditions.element_to_be_clickable(self.confirm_sms_code))
        confirm_sms_code.click()

    def get_sms(self):
        phone_number = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(self.click_phone_number))
        return phone_number.text

    #Tarjeta de credito
    def click_payment_method(self):
        payment_method = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.payment_method))
        payment_method.click()

    def click_button_add_credit_card(self):
        add_credit_card = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(self.add_credit_card))
        add_credit_card.click()

    def fill_card_and_code_number(self, card_number, card_code):
        add_card_number = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(self.add_card_number))
        add_card_number = self.driver.find_element(*self.add_card_number).send_keys(card_number + Keys.TAB + card_code)
        self.driver.find_element(*self.card_plc_image).click()

    def click_next_button_card(self):
        add_full_info_card = WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(self.add_full_info_card))
        add_full_info_card.click()

    def close_payment_method(self):
        close_method_card = WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(self.close_method_card))
        close_method_card.click()

    def credit_card_correct(self):
        confirm_credit_card_added = WebDriverWait(self.driver, 5).until(
        expected_conditions.visibility_of_element_located(self.confirm_credit_card_added))
        return confirm_credit_card_added.text

    #Mensaje para el conductor
    def click_box_for_message(self):
        box_message_for_driver = WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.box_message_for_driver))
        box_message_for_driver.click()

    def write_a_message_for_driver(self):
        box_message_for_driver = WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.box_message_for_driver))
        box_message_for_driver.send_keys(data.message_for_driver)

    #Ordenar mantas y pañuelos
    def order_blanket_handkerchiefs(self):
        order_blanket_and_handkerchiefs = self.driver.find_element(*self.order_blanket_and_handkerchiefs)
        order_blanket_and_handkerchiefs.click()

    def order_two_ice_cream(self):
        order_ice_cream_plus = self.driver.find_element(*self.order_ice_cream_plus)
        order_ice_cream_plus.click()
        order_ice_cream_plus.click()

    def for_search_modal_taxi(self):
        smart = WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.smart))
        smart.click()

    def wait_for_conductor_info(self):
        driver_modal = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(self.driver_modal))

