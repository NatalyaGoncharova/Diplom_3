import allure
from pages.page_object_login import *
from data import *


class TestLoginPage:

    @allure.title("Открытие страницы сброса пароля")
    def test_open_reset_page(self, driver):
        login_page = LoginPage(driver)
        with allure.step("Открываем URL страницы логина"):
            login_page.open_login_url()
        with allure.step("Нажимаем на ссылку сброса пароля"):
            login_page.click_reset_login_link()

        with allure.step("Проверяем, что URL изменился на URL сброса пароля"):
            assert login_page.get_current_url() == RESET_URL

    @allure.title("Заполнение email для сброса пароля")
    def test_fill_email_for_reset_password(self, driver):
        login_page = LoginPage(driver)
        with allure.step("Открываем URL страницы логина"):
            login_page.open_login_url()
        with allure.step("Нажимаем на ссылку сброса пароля"):
            login_page.click_reset_login_link()
        with allure.step("Заполняем email для сброса пароля"):
            login_page.fill_email_for_reset_password()

        with allure.step("Проверяем, что URL изменился на страницу подтверждения сброса пароля"):
            assert login_page.get_current_url(10) == RESET_PASSWORD_URL

    @allure.title("Проверка видимости пароля")
    def test_password_visibility(self, driver):
        login_page = LoginPage(driver)
        with allure.step("Открываем URL страницы логина"):
            login_page.open_login_url()
        with allure.step("Нажимаем на ссылку сброса пароля"):
            login_page.click_reset_login_link()
        with allure.step("Заполняем email для сброса пароля"):
            login_page.fill_email_for_reset_password()
        with allure.step("Ожидаем видимость поля для ввода пароля"):
            login_page.wait_for_visibility(RESET_PASSWORD_INPUT)
        with allure.step("Вводим новый пароль"):
            login_page.fill_password_for_reset()
        with allure.step("Ожидаем появления иконки показа пароля"):
            login_page.wait_for_visibility(EYE_ICON_ELEMENT)

        active_password = str(login_page.find_element(RESET_PASSWORD_INPUT).get_attribute("value"))
        with allure.step("Переключаем видимость пароля"):
            login_page.toggle_password_visibility()

        with allure.step("Проверяем, что введенный пароль соответствует ожидаемому значению"):
            assert active_password == NEW_PASSWORD
