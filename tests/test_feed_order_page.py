import allure
from pages.page_object_main import *
from data import *


class TestFeedOrderPage:

    @allure.title("Открытие модального окна заказа")
    def test_open_order_modal_window(self, create_order):
        order_page = create_order
        order_page.open_order()
        modal = order_page.wait_for_visibility(MODAL_ORDER)

        with allure.step("Проверка отображения модального окна"):
            assert modal.is_displayed()

    @allure.title("Проверка соответствия ID заказа в истории и ленте")
    def test_id_order_in_history_and_feed(self, create_order):
        order_page = create_order
        orders_from_history = order_page.get_list_orders_in_history()
        order_page.open_url(ORDER_FEED_URL)
        orders_from_feed = order_page.get_list_orders_in_feed()

        with allure.step("Проверка наличия ID заказа из истории в ленте"):
            for order_id in orders_from_history:
                assert order_id in orders_from_feed

    @allure.title("Проверка увеличения количества выполненных заказов")
    def test_get_completed_orders_count_increased(self, create_order_for_check_feed):
        order_page, count, today_count = create_order_for_check_feed
        upgrade_count = order_page.get_completed_orders_count()

        with allure.step("Сравнение увеличенного количества выполненных заказов"):
            assert upgrade_count > count

    @allure.title("Проверка увеличения количества заказов за сегодня")
    def test_get_completed_today_count_increased(self, create_order_for_check_feed):
        order_page, count, today_count = create_order_for_check_feed
        upgrade_today_count = order_page.get_completed_today_count()

        with allure.step("Сравнение увеличенного количества заказов за сегодня"):
            assert upgrade_today_count > today_count

    @allure.title("Проверка заказа в процессе выполнения")
    def test_get_orders_in_progress(self, create_order_1):
        order_page, order_number = create_order_1
        orders_in_progress = order_page.get_orders_in_progress()

        with allure.step("Проверка соответствия номера заказа в процессе выполнения"):
            assert int(orders_in_progress[0]) == int(order_number)
