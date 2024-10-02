import pytest
from selenium import webdriver
from class_user_api import *
from pages.page_object_feed_order import *
from pages.page_object_profile import *
from pages.page_object_main import *
from data import *


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome or firefox")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def create_and_delete_user():
    email = f'{fake.email()}test546'
    password = fake.password()
    name = fake.name()
    response = UserAuthorisation.registrate_user(email, password, name)
    access_token = response.json()['accessToken']
    yield email, password
    UserAuthorisation.delete_user(access_token)


@pytest.fixture
def create_order(driver, create_and_delete_user):
    email, password = create_and_delete_user
    order_page = FeedOrderPage(driver)
    profile_page = ProfilePage(driver)
    order = MainPage(driver)
    order_page.open_url(BASE_URL)
    order_page.login_user(email, password)
    order_page.wait_for_visibility(BUN2)
    order.add_ingredient_to_order()
    order.create_order()
    order.close_order_modal()
    profile_page.click_person_account_button()
    profile_page.open_history()
    yield order_page


@pytest.fixture
def create_order_for_check_feed(driver, create_and_delete_user):
    email, password = create_and_delete_user
    order_page = FeedOrderPage(driver)
    order = MainPage(driver)
    order_page.open_url(ORDER_FEED_URL)
    count = order_page.get_completed_orders_count()
    today_count = order_page.get_completed_today_count()
    order.open_constructor()
    order_page.login_user(email, password)
    order_page.wait_for_visibility(BUN2)
    order.add_ingredient_to_order()
    order.create_order()
    order.close_order_modal()
    order.open_order_feed()
    yield order_page, count, today_count


@pytest.fixture
def create_order_1(driver, create_and_delete_user):
    email, password = create_and_delete_user
    order_page = FeedOrderPage(driver)
    order = MainPage(driver)
    order_page.open_url(BASE_URL)
    order_page.login_user(email, password)
    order_page.wait_for_visibility(BUN2)
    order.add_ingredient_to_order()
    order.create_order()
    order_number = order.get_order_number()
    order.close_order_modal()
    order.open_order_feed()
    yield order_page, order_number
