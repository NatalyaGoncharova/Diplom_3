from selenium.webdriver.common.by import By

LIST_ORDER_ID = (By.XPATH, "//p[contains(@class, 'text_type_digits-default')]")

FEED_ORDER_ID = (By.XPATH, "//p[contains(@class, 'text_type_digits-default')]")

ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")

COMPLETED_ORDERS_COUNT = (By.XPATH, '//p[contains(@class, "text_type_digits-large")]')

ORDERS_IN_PROGRESS = (By.XPATH,"//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'text_type_digits-default')]")

COMPLETED_TODAY = (By.XPATH, '//p[contains(text(), "Выполнено за сегодня")]/following-sibling::p')

ORDER_DETAIL = (By.CSS_SELECTOR, "ul.OrderHistory_profileList__374GU li:first-child a")

MODAL_ORDER = (By.CSS_SELECTOR, "[class*='Modal_orderBox']")