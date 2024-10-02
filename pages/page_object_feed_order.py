from locators.feed_orders_locators import *
from pages.base_page import BasePage


class FeedOrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_order(self):
        self.wait_for_visibility(ORDER_DETAIL)
        self.find_element(ORDER_DETAIL).click()

    def get_list_orders_in_history(self):
        self.wait_for_visibility(LIST_ORDER_ID)
        order_ids_elements = self.driver.find_elements(*LIST_ORDER_ID)
        order_ids = [element.text for element in order_ids_elements]
        return order_ids

    def get_list_orders_in_feed(self):
        self.wait_for_visibility(FEED_ORDER_ID)
        feed_order_ids_elements = self.driver.find_elements(*FEED_ORDER_ID)
        feed_order_ids = [element.text for element in feed_order_ids_elements]
        return feed_order_ids

    def get_completed_orders_count(self):
        self.wait_for_visibility(COMPLETED_ORDERS_COUNT)
        completed_orders_element = self.driver.find_element(*COMPLETED_ORDERS_COUNT)
        completed_orders_count = completed_orders_element.text
        return completed_orders_count

    def get_completed_today_count(self):
        self.wait_for_visibility(COMPLETED_TODAY)
        completed_today_element = self.driver.find_element(*COMPLETED_TODAY)
        completed_today_count = completed_today_element.text

        return completed_today_count

    def get_orders_in_progress(self):
        self.wait_for_visibility(ORDERS_IN_PROGRESS)
        orders_elements = self.driver.find_elements(*ORDERS_IN_PROGRESS)
        orders_in_progress = [element.text for element in orders_elements]
        return orders_in_progress
