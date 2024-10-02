from locators.login_locators import *
from pages.base_page import BasePage
from data import *


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_reset_login_link(self):
        self.click(RESET_PASSWORD_LINK)

    def click_forgot_password(self):
        self.find_element(RESET_BUTTON).click()

    def fill_email_for_reset_password(self):
        self.find_element(RESET_PASSWORD_EMAIL_INPUT).send_keys(EMAIL)
        self.find_element(RESET_BUTTON).click()

    def fill_password_for_reset(self):
        self.find_element(RESET_PASSWORD_INPUT).send_keys(NEW_PASSWORD)

    def toggle_password_visibility(self):
        self.find_element(EYE_ICON_ELEMENT).click()

    def is_password_field_active(self):
        return "active" in self.driver.find_element(RESET_PASSWORD_INPUT).get_attribute("value")
