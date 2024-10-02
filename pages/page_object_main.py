from locators.main_page_locators import *
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_constructor(self):
        constructor_button = self.wait_for_clickable(CONSTRUCTOR_BUTTON)
        constructor_button.click()

    def open_order_feed(self):
        self.find_element(ORDER_FEED_BUTTON).click()

    def click_ingredient(self):
        self.find_element(BUN1).click()

    def close_pop_up(self):
        self.find_element(CLOSE_POP_UP_BUTTON).click()

    def add_ingredient_to_order(self):
        ingredient = self.find_element(BUN2)
        order_area = self.find_element(ORDER_AREA)
        ActionChains(self.driver).drag_and_drop(ingredient, order_area).perform()

    def get_ingredient_counter(self):
        counter_element = self.find_element(COUNTER)
        return int(counter_element.text)

    def create_order(self):
        self.find_element(ORDER_BUTTON).click()

    def close_order_modal(self):
        self.wait_for_clickable(CLOSE_MODAL_ORDER)
        self.wait_for_modal_loading_to_disappear(MODAL_LOADING)
        self.find_element(CLOSE_MODAL_ORDER).click()

    def get_order_number(self):
        self.wait_for_visibility(ORDER_NUMBER)
        old_order_number = self.driver.find_element(*ORDER_NUMBER).text
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*ORDER_NUMBER).text != old_order_number
        )
        new_order_number = self.driver.find_element(*ORDER_NUMBER).text

        return new_order_number

