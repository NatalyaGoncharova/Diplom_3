import allure
from pages.page_object_main import *
from data import *

class TestMainPage:

    @allure.title("Открытие страницы конструктора")
    def test_open_constructor_page(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открываем страницу логина"):
            main_page.open_login_url()
        with allure.step("Переходим на страницу конструктора"):
            main_page.open_constructor()

        with allure.step("Проверяем, что URL соответствует базовому"):
            assert main_page.get_current_url() == BASE_URL

    @allure.title("Открытие страницы ленты заказов")
    def test_open_order_feed_page(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открываем базовый URL"):
            main_page.open_base_url()
        with allure.step("Переходим на страницу ленты заказов"):
            main_page.open_order_feed()

        with allure.step("Проверяем, что URL соответствует странице ленты заказов"):
            assert main_page.get_current_url() == ORDER_FEED_URL

    @allure.title("Открытие деталей ингредиента")
    def test_open_details_of_ingredients(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открываем базовый URL"):
            main_page.open_base_url()
        with allure.step("Нажимаем на ингредиент для открытия его деталей"):
            main_page.click_ingredient()

        with allure.step("Проверяем, что URL соответствует странице ингредиента"):
            assert main_page.get_current_url() == INGREDIENT1_URL

    @allure.title("Закрытие попапа с деталями ингредиента")
    def test_close_pop_up_detail_of_ingredients(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открываем базовый URL"):
            main_page.open_base_url()
        with allure.step("Открываем детали ингредиента"):
            main_page.click_ingredient()
        with allure.step("Закрываем попап"):
            main_page.close_pop_up()
        is_pop_up_closed = main_page.wait_for_element(CLOSE_POP_UP_BUTTON)

        with allure.step("Проверяем, что попап закрыт"):
            assert is_pop_up_closed

    @allure.title("Увеличение счетчика ингредиентов после добавления")
    def test_add_ingredient_increases_counter(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открываем базовый URL"):
            main_page.open_base_url()
        with allure.step("Получаем текущий счетчик ингредиентов"):
            initial_counter = main_page.get_ingredient_counter()
        with allure.step("Добавляем ингредиент в заказ"):
            main_page.add_ingredient_to_order()
        with allure.step("Ожидаем появления счетчика"):
            main_page.wait_for_visibility(COUNTER)
        new_counter = main_page.get_ingredient_counter()

        with allure.step("Проверяем, что счетчик увеличился на 2"):
            assert new_counter == initial_counter + 2

    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_by_authorised_user(self, driver):
        main_page = MainPage(driver)
        email = EMAIL
        password = PASSWORD
        with allure.step("Открываем базовый URL"):
            main_page.open_base_url()
        with allure.step("Авторизуем пользователя"):
            main_page.login_user(email, password)
        with allure.step("Добавляем ингредиент в заказ"):
            main_page.wait_for_visibility(BUN2)
            main_page.add_ingredient_to_order()
        with allure.step("Создаем заказ"):
            main_page.create_order()

        order_number_element = main_page.wait_for_visibility(ORDER_NUMBER)
        order_number = order_number_element.text

        with allure.step("Проверяем, что номер заказа является числом"):
            assert order_number.isdigit()








