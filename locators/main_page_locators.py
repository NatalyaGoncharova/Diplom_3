from selenium.webdriver.common.by import By

ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history' and contains(text(), 'История заказов')]")

LIST_ORDER_ID = (By.XPATH, "//p[contains(@class, 'text_type_digits-default')]")

FEED_ORDER_ID = (By.XPATH, "//p[contains(@class, 'text_type_digits-default')]")

ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")

BUN1 = (By.XPATH, "//p[text()='Краторная булка N-200i']")

CLOSE_POP_UP_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")

BUN2 = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[1]/a[1]")

COUNTER = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[1]/a[1]/div[1]/p")

ORDER_AREA = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")

AMOUNT_ORDER = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/div/p")

ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Оформить заказ']")

ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__2L34m')]")

ORDER_DETAIL = (By.CSS_SELECTOR, "ul.OrderHistory_profileList__374GU li:first-child a")

MODAL_ORDER = (By.CSS_SELECTOR, "[class*='Modal_orderBox']")

CLOSE_MODAL_ORDER = (By.XPATH, "/html/body/div/div/section/div[1]/button")

MODAL_LOADING = (By.XPATH, "//img[contains(@class, 'Modal_modal__loading')]")

CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@href='/' and contains(@class, 'AppHeader_header__link')]")