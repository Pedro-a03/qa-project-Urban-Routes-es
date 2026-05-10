import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    call_taxi_button = (By.CLASS_NAME, 'round')
    comfort_tariff_button = (By.XPATH, "//div[contains(@class,'tcard') and .//div[text()='Comfort']]")
    phone_number_field = (By.CLASS_NAME, 'np-button')
    phone_input = (By.ID, 'phone')
    next_button = (By.XPATH, "//button[text()='Siguiente']")
    code_input = (By.ID, 'code')
    confirm_button = (By.XPATH, "//button[text()='Confirmar']")
    message_field = (By.ID, 'comment')
    blanket_and_tissues_switch = (By.XPATH,
                                  "//div[@class='r-sw-container' and .//div[text()='Manta y pañuelos']]//span[@class='slider round']")
    blanket_and_tissues_checkbox = (By.XPATH,
                                    "//div[@class='r-sw-container' and .//div[text()='Manta y pañuelos']]//input[@type='checkbox']")
    ice_cream_plus_button = (By.XPATH,
                             "//div[@class='r-counter-container' and .//div[text()='Helado']]//div[@class='counter-plus']")
    ice_cream_counter = (By.XPATH,
                         "//div[@class='r-counter-container' and .//div[text()='Helado']]//div[@class='counter-value']")
    order_taxi_button = (By.CSS_SELECTOR, 'button.smart-button')
    driver_arrival_modal = (By.CLASS_NAME, 'order-header-title')
    payment_method_button = (By.CLASS_NAME, 'pp-text')
    add_card_button = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    card_number_input = (By.ID, 'number')
    card_code_input = (By.CSS_SELECTOR, 'input.card-input[id="code"]')
    add_card_submit_button = (By.XPATH, "//button[text()='Agregar']")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.from_field)
        )
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.to_field)
        )
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def click_call_taxi_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.call_taxi_button)
        )
        self.driver.find_element(*self.call_taxi_button).click()

    def select_comfort_tariff(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.comfort_tariff_button)
        )
        self.driver.find_element(*self.comfort_tariff_button).click()

    def click_phone_number_field(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.phone_number_field)
        )
        self.driver.find_element(*self.phone_number_field).click()

    def set_phone_number(self, phone_number):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.phone_input)
        )
        self.driver.find_element(*self.phone_input).send_keys(phone_number)

    def click_next_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.next_button)
        )
        self.driver.find_element(*self.next_button).click()

    def set_phone_code(self, code):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.code_input)
        )
        self.driver.find_element(*self.code_input).send_keys(code)

    def click_confirm_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.confirm_button)
        )
        self.driver.find_element(*self.confirm_button).click()

    def set_message_for_driver(self, message):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.message_field)
        )
        self.driver.find_element(*self.message_field).send_keys(message)

    def click_blanket_and_tissues_switch(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.blanket_and_tissues_switch)
        )
        self.driver.find_element(*self.blanket_and_tissues_switch).click()

    def is_blanket_and_tissues_selected(self):
        return self.driver.find_element(*self.blanket_and_tissues_checkbox).is_selected()

    def order_two_ice_creams(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.ice_cream_plus_button)
        )
        for _ in range(2):
            self.driver.find_element(*self.ice_cream_plus_button).click()

    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ice_cream_counter).text

    def click_order_taxi_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.order_taxi_button)
        )
        self.driver.find_element(*self.order_taxi_button).click()

    def wait_for_driver_info(self):
        WebDriverWait(self.driver, 60).until(
            expected_conditions.visibility_of_element_located(self.driver_arrival_modal)
        )
        return self.driver.find_element(*self.driver_arrival_modal).text

    def click_payment_method_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.payment_method_button)
        )
        self.driver.find_element(*self.payment_method_button).click()

    def click_add_card_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.add_card_button)
        )
        self.driver.find_element(*self.add_card_button).click()

    def set_card_number(self, card_number):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.card_number_input)
        )
        self.driver.find_element(*self.card_number_input).send_keys(card_number)

    def set_card_code(self, card_code):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.card_code_input)
        )
        self.driver.find_element(*self.card_code_input).send_keys(card_code)
        self.driver.find_element(*self.card_code_input).send_keys(Keys.TAB)

    def click_add_card_submit(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.add_card_submit_button)
        )
        self.driver.find_element(*self.add_card_submit_button).click()

    def add_credit_card(self, card_number, card_code):
        self.click_payment_method_button()
        self.click_add_card_button()
        self.set_card_number(card_number)
        self.set_card_code(card_code)
        self.click_add_card_submit()

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')


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

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort_tariff(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.click_call_taxi_button()
        routes_page.select_comfort_tariff()

    def test_set_phone_number(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.click_call_taxi_button()
        routes_page.select_comfort_tariff()
        routes_page.click_phone_number_field()
        routes_page.set_phone_number(data.phone_number)
        routes_page.click_next_button()
        code = retrieve_phone_code(self.driver)
        routes_page.set_phone_code(code)
        routes_page.click_confirm_button()

    def test_set_message_for_driver(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.click_call_taxi_button()
        routes_page.select_comfort_tariff()
        routes_page.click_phone_number_field()
        routes_page.set_phone_number(data.phone_number)
        routes_page.click_next_button()
        code = retrieve_phone_code(self.driver)
        routes_page.set_phone_code(code)
        routes_page.click_confirm_button()
        routes_page.set_message_for_driver(data.message_for_driver)

    def test_request_blanket_and_tissues(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.click_call_taxi_button()
        routes_page.select_comfort_tariff()
        routes_page.click_phone_number_field()
        routes_page.set_phone_number(data.phone_number)
        routes_page.click_next_button()
        code = retrieve_phone_code(self.driver)
        routes_page.set_phone_code(code)
        routes_page.click_confirm_button()
        routes_page.set_message_for_driver(data.message_for_driver)
        routes_page.click_blanket_and_tissues_switch()
        assert routes_page.is_blanket_and_tissues_selected() is True

    def test_order_two_ice_creams(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.click_call_taxi_button()
        routes_page.select_comfort_tariff()
        routes_page.click_phone_number_field()
        routes_page.set_phone_number(data.phone_number)
        routes_page.click_next_button()
        code = retrieve_phone_code(self.driver)
        routes_page.set_phone_code(code)
        routes_page.click_confirm_button()
        routes_page.set_message_for_driver(data.message_for_driver)
        routes_page.click_blanket_and_tissues_switch()
        routes_page.order_two_ice_creams()
        assert routes_page.get_ice_cream_count() == '2'

    def test_order_taxi(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.click_call_taxi_button()
        routes_page.select_comfort_tariff()
        routes_page.click_phone_number_field()
        routes_page.set_phone_number(data.phone_number)
        routes_page.click_next_button()
        code = retrieve_phone_code(self.driver)
        routes_page.set_phone_code(code)
        routes_page.click_confirm_button()
        routes_page.click_order_taxi_button()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(routes_page.driver_arrival_modal)
        )

    def test_add_credit_card(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.click_call_taxi_button()
        routes_page.select_comfort_tariff()
        routes_page.click_phone_number_field()
        routes_page.set_phone_number(data.phone_number)
        routes_page.click_next_button()
        code = retrieve_phone_code(self.driver)
        routes_page.set_phone_code(code)
        routes_page.click_confirm_button()
        routes_page.add_credit_card(data.card_number, data.card_code)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
