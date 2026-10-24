from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Products are present in the basket, but should not be"

    def should_be_empty_basket_text(self):
        text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert "пуста" in text.lower() or "empty" in text.lower(), \
            "Empty basket text is not presented"