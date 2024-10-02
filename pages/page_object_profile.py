from locators.profile_locators import *
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_person_account_button(self):
        self.find_element(PROFILE_ELEMENT).click()

    def open_history(self):
        self.wait_for_element(ORDER_HISTORY_LINK)
        self.find_element(ORDER_HISTORY_LINK).click()

    def logout_user(self):
        self.find_element(LOGOUT_BUTTON).click()



