import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    # Localizadores
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    call_taxi_button = (By.CLASS_NAME, 'round')
    comfort_tariff_button = (By.XPATH, "//div[contains(@class,'tcard') and .//div[text()='Comfort']]")
    comfort_tariff_selected = (By.XPATH, "//div[contains(@class,'tcard') and contains(@class,'active') and .//div[text()='Comfort']]")
    phone_number_field = (By.CLASS_NAME, 'np-button')
    phone_number_displayed = (By.CLASS_NAME, 'np-text')
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
    payment_method_button = (By.CSS_SELECTOR, 'div.pp-button.filled')
    add_card_button = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    card_number_input = (By.CSS_SELECTOR, 'input.card-input[id="number"]')
    card_code_input = (By.CSS_SELECTOR, 'input.card-input[id="code"]')
    add_card_submit_button = (By.CSS_SELECTOR, 'button.button.full')
    card_added_label = (By.XPATH, "//div[@class='pp-title' and text()='Tarjeta']")
    close_modal_button = (By.CSS_SELECTOR, 'button.close-button.section-close')
    close_phone_modal_button = (By.CSS_SELECTOR, '.modal .section.active button.close-button.section-close')
    overlay = (By.CLASS_NAME, 'overlay')

    def __init__(self, driver):
        self.driver = driver

    # --- Métodos de acción ---

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

    def order_two_ice_creams(self):
        self.wait_for_overlays_to_disappear()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.ice_cream_plus_button)
        )
        for _ in range(2):
            self.click_with_js(self.ice_cream_plus_button)

    def click_order_taxi_button(self):
        self.wait_for_overlays_to_disappear()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.order_taxi_button)
        )
        self.click_with_js(self.order_taxi_button)

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
        field = self.driver.find_element(*self.card_number_input)
        field.click()
        field.clear()
        for char in card_number:
            ActionChains(self.driver).send_keys(char).perform()
            time.sleep(0.1)

    def set_card_code(self, card_code):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.card_code_input)
        )
        field = self.driver.find_element(*self.card_code_input)
        field.click()
        field.clear()
        for char in card_code:
            ActionChains(self.driver).send_keys(char).perform()
            time.sleep(0.1)
        ActionChains(self.driver).send_keys(Keys.TAB).perform()

    def click_add_card_submit(self):
        time.sleep(3)
        self.driver.execute_script(
            "document.querySelectorAll('button.button.full')[3].click();"
        )

    def add_credit_card(self, card_number, card_code):
        self.click_payment_method_button()
        self.click_add_card_button()
        self.set_card_number(card_number)
        self.set_card_code(card_code)
        self.click_add_card_submit()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located(self.card_added_label)
        )

    def close_phone_modal(self):
        try:
            WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.modal'))
            )
            close_button = WebDriverWait(self.driver, 5).until(
                expected_conditions.element_to_be_clickable(self.close_phone_modal_button)
            )
            close_button.click()
            WebDriverWait(self.driver, 5).until(
                expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, '.modal'))
            )
        except Exception:
            pass

    def wait_for_overlays_to_disappear(self):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.invisibility_of_element_located(self.overlay)
            )
        except Exception:
            pass
        time.sleep(1)

    def click_with_js(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def click_blanket_and_tissues_switch(self):
        self.wait_for_overlays_to_disappear()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.blanket_and_tissues_switch)
        )
        self.click_with_js(self.blanket_and_tissues_switch)

    # --- Métodos getter / checker para asserts ---

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def is_comfort_selected(self):
        elements = self.driver.find_elements(*self.comfort_tariff_selected)
        return len(elements) > 0

    def get_phone_number(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.phone_number_displayed)
        )
        return self.driver.find_element(*self.phone_number_displayed).text

    def get_message_text(self):
        return self.driver.find_element(*self.message_field).get_property('value')

    def is_blanket_and_tissues_selected(self):
        return self.driver.find_element(*self.blanket_and_tissues_checkbox).is_selected()

    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ice_cream_counter).text

    def is_driver_arrival_modal_visible(self):
        elements = self.driver.find_elements(*self.driver_arrival_modal)
        return len(elements) > 0

    def wait_for_driver_info(self):
        WebDriverWait(self.driver, 60).until(
            expected_conditions.visibility_of_element_located(self.driver_arrival_modal)
        )
        return self.driver.find_element(*self.driver_arrival_modal).text

    def is_card_added(self):
        elements = self.driver.find_elements(*self.card_added_label)
        return len(elements) > 0

    def close_payment_modal(self):
        try:
            self.driver.execute_script(
                "document.querySelector('.modal .section.active button.close-button').click();"
            )
            WebDriverWait(self.driver, 5).until(
                expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, '.modal'))
            )
        except Exception:
            pass


