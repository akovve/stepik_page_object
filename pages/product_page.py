from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        button.click()
        # Решаем капчу (вызов метода из BasePage)
        self.solve_quiz_and_get_code()

    # Метод для получения названия товара со страницы
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    # Метод для получения цены товара со страницы
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    # Проверка, что имя в сообщении совпадает с ожидаемым
    def should_be_product_name_in_success_message(self, expected_name):
        success_msg_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MSG_NAME).text
        assert success_msg_name == expected_name, \
            f"Ожидалось имя '{expected_name}', но в сообщении '{success_msg_name}'"

    # Проверка, что цена в сообщении совпадает с ожидаемой
    def should_be_product_price_in_basket_message(self, expected_price):
        basket_msg_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MSG).text
        assert basket_msg_price == expected_price, \
            f"Ожидалась цена '{expected_price}', но в сообщении '{basket_msg_price}'"