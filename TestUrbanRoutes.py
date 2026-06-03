from gc import enable

import data
from selenium import webdriver
from UrbanRoutesPage import UrbanRoutesPage
from helpers import retrieve_phone_code

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_select_comfort(self):
        assert self.routes_page.is_enabled_req_cap() == True
        self.routes_page.click_req_cap()
        assert self.routes_page.is_enabled_select_comfort() == True
        self.routes_page.click_select_comfort()
        assert 'active' in self.routes_page.is_selected_comfort()

    def test_select_phone_number(self):
        assert self.routes_page.is_enabled_add_phone() == True
        self.routes_page.click_add_phone()
        self.routes_page.set_phone(data.phone_number)
        assert self.routes_page.get_phone() == data.phone_number
        assert self.routes_page.is_enabled_sel_next() == True
        self.routes_page.click_sel_next()
        code = retrieve_phone_code(self.driver)
        self.routes_page.set_phone_code(code)
        self.routes_page.click_conf_phone()
        assert self.routes_page.get_phone_number_added() == data.phone_number

    def test_payment_method(self):
        assert self.routes_page.is_enabled_payment_method() == True
        self.routes_page.click_payment_method()
        assert self.routes_page.is_enabled_select_debit() == True
        self.routes_page.click_select_debit()
        self.routes_page.set_debit_number(data.card_number)
        assert self.routes_page.get_debit_number() == data.card_number
        self.routes_page.set_code(data.card_code)
        assert self.routes_page.get_code() == data.card_code
        assert self.routes_page.is_enabled_sel_add_debit() == True
        self.routes_page.click_sel_add_debit()
        assert self.routes_page.is_enabled_cl_debit_card() == True
        self.routes_page.click_cl_debit_card()

    def test_driver(self):
        assert self.routes_page.is_enabled_mns_driver() == True
        self.routes_page.click_mns_driver()
        self.routes_page.set_mns_driver(data.message_for_driver)
        assert self.routes_page.get_mns_driver() == data.message_for_driver

    def test_driver_tissue(self):
        assert self.routes_page.is_enabled_blanket_tissue() == True
        self.routes_page.click_blanket_tissue()
        assert self.routes_page.is_checked_blanket_tissue() == True

    def test_driver_ice_cream(self):
        assert self.routes_page.is_enabled_ice_cream() == True
        self.routes_page.add_ice_cream(data.ice_cream_quantity)
        assert self.routes_page.get_ice_cream_quantity_added() == str(data.ice_cream_quantity)

    def test_req_ride(self):
        assert self.routes_page.is_enabled_request_taxi() == True
        self.routes_page.click_request_taxi_cap()

    def test_driver_wait_time(self):
        self.routes_page.wait_driver_assigned()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
