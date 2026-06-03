import self
import data
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page import UrbanRoutesPage
import  helpers

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service, options=options)

#pasos a seguir para hacer la prueba

    def test_set_route_from_and_to(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route_from()
        routes_page.set_route_to()
        assert routes_page.get_from() == data.address_from
        assert routes_page.get_to() == data.address_to

    def test_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_a_taxi()
        routes_page.comfort_the_tariff_button()
        assert routes_page.comfort_the_tariff_button() == 'Comfort'

    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.open_phone_number_box()
        routes_page.write_phone_number(data.phone_number)
        routes_page.next_button()
        sms = helpers.retrieve_phone_code(self.driver)
        routes_page.fill_sms_code(sms)
        routes_page.confirm_button_sms_code()
        assert routes_page.get_phone_number() == '+1 123 123 12 12'
    def test_configurate_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_payment_method()
        routes_page.click_button_add_credit_card()
        routes_page.fill_card_and_code_number(data.card_number, data.card_code)
        routes_page.click_next_button_card()
        routes_page.close_payment_method()
        assert routes_page.credit_card_correct() == 'Tarjeta'

    def test_write_message_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_box_for_message()
        routes_page.write_a_message_for_driver()
        #confirmar que el mensaje se escribio correctamente
       # assert UrbanRoutesPage.write_a_message_for_driver == 'Muéstrame el camino al museo'

    def test_order_blanket_handkerchiefs(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_blanket_and_handkerchiefs()

    def test_order_two_ice_cream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_two_ice_cream
        # verificar que se hayan pedido los 2 helados
        assert UrbanRoutesPage.order_two_ice_cream() == 2

    def test_taxi_search_modal_appears(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.for_search_modal_taxi()
        routes_page.wait_for_conductor_info()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()