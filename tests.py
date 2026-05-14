import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import retrieve_phone_code
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # Modificado por compatibilidad con Selenium 4.x y Chrome 147 (aprobado por IA Tripleten)
        # Usando set_capability para goog:loggingPrefs (capacidad W3C estándar)
        # en lugar de add_experimental_option para compatibilidad con Selenium 4.x
        # Mantiene la habilitación de logs de performance necesaria para retrieve_phone_code()
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    # Test 1 — Acción 1: Establecer ruta
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        self.routes_page.set_route(data.address_from, data.address_to)
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    # Test 2 — Acción 2: Seleccionar tarifa Comfort
    def test_select_comfort_tariff(self):
        self.routes_page.click_call_taxi_button()
        self.routes_page.select_comfort_tariff()
        assert self.routes_page.is_comfort_selected() is True

    # Test 3 — Acción 3: Ingresar número de teléfono
    def test_set_phone_number(self):
        self.routes_page.click_phone_number_field()
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.click_next_button()
        code = retrieve_phone_code(self.driver)
        self.routes_page.set_phone_code(code)
        self.routes_page.click_confirm_button()
        self.routes_page.close_phone_modal()
        assert self.routes_page.get_phone_number() == data.phone_number

    # Test 4 — Acción 4: Agregar tarjeta de crédito
    def test_add_credit_card(self):
        self.routes_page.add_credit_card(data.card_number, data.card_code)
        assert self.routes_page.is_card_added() is True
        self.routes_page.close_payment_modal()

    # Test 5 — Acción 5: Escribir mensaje para el conductor
    def test_set_message_for_driver(self):
        self.routes_page.set_message_for_driver(data.message_for_driver)
        assert self.routes_page.get_message_text() == data.message_for_driver

    # Test 6 — Acción 6: Pedir manta y pañuelos
    def test_request_blanket_and_tissues(self):
        self.routes_page.click_blanket_and_tissues_switch()
        assert self.routes_page.is_blanket_and_tissues_selected() is True

    # Test 7 — Acción 7: Pedir 2 helados
    def test_order_two_ice_creams(self):
        self.routes_page.order_two_ice_creams()
        assert self.routes_page.get_ice_cream_count() == data.ice_cream_count

    # Test 8 — Acción 8: Hacer clic en el botón de pedir taxi
    def test_click_order_taxi_button(self):
        self.routes_page.click_order_taxi_button()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(self.routes_page.driver_arrival_modal)
        )
        assert self.routes_page.is_driver_arrival_modal_visible() is True

    # Test 9 — Acción 9: Esperar información del conductor
    def test_wait_for_driver_info(self):
        driver_info = self.routes_page.wait_for_driver_info()
        assert driver_info is not None and len(driver_info) > 0

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

