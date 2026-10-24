from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        button.click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_product_name_in_success_message(self):
        expected_name = self.get_product_name()
        success_msg_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MSG_NAME).text
        assert success_msg_name == expected_name, \
            f"Ожидалось имя '{expected_name}', но в сообщении '{success_msg_name}'"

    def should_be_product_price_in_basket_message(self):
        expected_price = self.get_product_price()
        basket_msg_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MSG).text
        assert basket_msg_price == expected_price, \
            f"Ожидалась цена '{expected_price}', но в сообщении '{basket_msg_price}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MSG_NAME), \
            "Success message is presented, but should not be"