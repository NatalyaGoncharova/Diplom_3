import allure
from pages.page_object_profile import *
from data import *

class TestPersonPage:

    @allure.title("Открытие страницы профиля")
    def test_open_profile_page(self, driver):
        profile_page = ProfilePage(driver)
        with allure.step("Открываем базовый URL"):
            profile_page.open_base_url()
        with allure.step("Нажимаем на кнопку аккаунта"):
            profile_page.click_person_account_button()

        with allure.step("Проверяем, что происходит редирект на страницу логина"):
            assert profile_page.get_current_url() == LOGIN_URL

    @allure.title("Открытие страницы истории заказов")
    def test_open_order_history_page(self, driver):
        profile_page = ProfilePage(driver)
        email = EMAIL
        password = PASSWORD
        with allure.step("Открываем базовый URL"):
            profile_page.open_base_url()
        with allure.step("Авторизуем пользователя"):
            profile_page.login_user(email, password)
        with allure.step("Нажимаем на кнопку аккаунта"):
            profile_page.click_person_account_button()
        with allure.step("Ожидаем появления ссылки на историю заказов"):
            profile_page.wait_for_element(ORDER_HISTORY_LINK)
        with allure.step("Переходим на страницу истории заказов"):
            profile_page.open_history()

        with allure.step("Проверяем, что URL соответствует странице истории заказов"):
            assert profile_page.get_current_url() == ORDER_HISTORY_URL

    @allure.title("Выход из аккаунта")
    def test_logout_user(self, driver):
        profile_page = ProfilePage(driver)
        email = EMAIL
        password = PASSWORD
        with allure.step("Открываем базовый URL"):
            profile_page.open_base_url()
        with allure.step("Авторизуем пользователя"):
            profile_page.login_user(email, password)
        with allure.step("Нажимаем на кнопку аккаунта"):
            profile_page.click_person_account_button()
        with allure.step("Ожидаем появления кнопки выхода"):
            profile_page.wait_for_element(LOGOUT_BUTTON)
        with allure.step("Нажимаем кнопку выхода из аккаунта"):
            profile_page.logout_user()

        with allure.step("Проверяем, что произошел редирект на страницу логина"):
            assert profile_page.get_current_url(10) == LOGIN_URL