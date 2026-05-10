# Urban Routes - QA Automation Project

[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.43.0-green.svg)](https://www.selenium.dev/)
[![pytest](https://img.shields.io/badge/pytest-9.0.3-orange.svg)](https://docs.pytest.org/)

## 📋 Project Description

This project is the final assignment of Sprint 9 of the QA Engineering bootcamp at TripleTen. The goal is to automate the end-to-end functional testing of **Urban Routes**, a web application that allows users to request taxi rides.

The automated test suite covers the complete user flow of ordering a taxi, including:

- Setting pickup and destination addresses
- Selecting the Comfort fare tier
- Filling in the user's phone number and verification code
- Adding a credit card with CVV confirmation
- Writing a custom message for the driver
- Requesting additional services (blanket, tissues, ice creams)
- Verifying the taxi search modal and driver assignment

The project follows industry-standard QA automation practices, including the **Page Object Model (POM)** design pattern and explicit waits for handling asynchronous page elements.

## 🛠️ Technologies and Tools

- **Programming Language:** Python 3.14
- **Test Automation Framework:** Selenium WebDriver 4.43.0
- **Test Runner:** pytest 9.0.3
- **Browser:** Google Chrome 147
- **Driver Management:** Selenium Manager (automatic ChromeDriver provisioning)
- **Version Control:** Git / GitHub
- **IDE:** PyCharm Community Edition
- **Operating System:** Windows 11

## 🧪 Testing Techniques and Patterns

This project applies the following QA automation techniques:

- **Page Object Model (POM):** UI elements and interactions are encapsulated in the `UrbanRoutesPage` class, separating test logic from page structure.
- **Explicit Waits:** `WebDriverWait` combined with `expected_conditions` ensures stable interactions with dynamically loaded elements, avoiding flaky tests.
- **Test Fixtures:** Class-level setup (`setup_class`) and teardown (`teardown_class`) manage the WebDriver lifecycle efficiently.
- **W3C Capabilities:** Performance logs (`goog:loggingPrefs`) are enabled via `set_capability` to intercept network responses required for the phone confirmation flow.
- **Network Log Interception:** The `retrieve_phone_code()` helper uses Chrome DevTools Protocol (CDP) to capture the SMS confirmation code from API responses.
- **Diverse Locator Strategies:** Tests use multiple Selenium locator types (`By.ID`, `By.CLASS_NAME`, `By.CSS_SELECTOR`, `By.XPATH`) to demonstrate flexible element identification.

## 📁 Project Structure

    qa-project-Urban-Routes-es/
    ├── .venv/                  # Virtual environment (not tracked in Git)
    ├── data.py                 # Test data: URL, addresses, phone, card details
    ├── main.py                 # Page Object class and test cases
    ├── README.md               # Project documentation
    └── .gitignore              # Files excluded from version control

## 👤 Author

**Pedro Acosta**

GitHub: [@Pedro-a03](https://github.com/Pedro-a03)