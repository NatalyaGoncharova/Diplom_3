from selenium.webdriver.common.by import By

RESET_PASSWORD_LINK = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a')

RESET_PASSWORD_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")

RESET_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")

RESET_PASSWORD_INPUT = (By.XPATH, '//input[@type="password" and @name="Введите новый пароль"]')

EYE_ICON_ELEMENT = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/div")

LOGIN_EMAIL_INPUT = (By.NAME, "name")

LOGIN_PASSWORD_INPUT = (By.NAME, "Пароль")

LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")

LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history' and contains(text(), 'История заказов')]")

LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")