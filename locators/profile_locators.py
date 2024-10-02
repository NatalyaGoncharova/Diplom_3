from selenium.webdriver.common.by import By


PROFILE_ELEMENT = (By.XPATH, "//p[text()='Личный Кабинет']")

ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history' and contains(text(), 'История заказов')]")

LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
