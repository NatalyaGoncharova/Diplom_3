from selenium.common import NoSuchWindowException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *
from locators.login_locators import *


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def login_user(self, email, password):
        self.find_element(LOGIN_ACCOUNT_BUTTON).click()
        self.find_element(LOGIN_EMAIL_INPUT).send_keys(email)
        self.find_element(LOGIN_PASSWORD_INPUT).send_keys(password)
        self.find_element(LOGIN_SUBMIT_BUTTON).click()

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def wait_for_visibility(self, locator):
        if isinstance(locator, tuple):
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        else:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of(locator))

    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def wait_for_modal_loading_to_disappear(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_current_url(self, timeout=None):
        if timeout:
            WebDriverWait(self.driver, timeout).until(EC.url_changes(self.driver.current_url))
        else:
            pass
        return self.driver.current_url

    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        new_window = self.driver.window_handles[-1]
        try:
            self.driver.switch_to.window(new_window)
        except NoSuchWindowException:
            WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
            self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_for_url_to_contain(self, url_fragment):
        WebDriverWait(self.driver, 10).until(EC.url_contains(url_fragment))

    def find_elements(self, by_locator):
        return self.driver.find_elements(*by_locator)

    def find_element(self, by_locator):
        return self.driver.find_element(*by_locator)

    def open_base_url(self):
        self.driver.get(BASE_URL)

    def open_login_url(self):
        self.driver.get(LOGIN_URL)

    def open_url(self, url):
        self.driver.get(url)
