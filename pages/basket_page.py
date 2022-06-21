from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    
    def should_message_empty_basket_shown(self):
        expected_message = "Your basket is empty."
        received_message = self.get_element_text(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        assert expected_message in received_message, \
               f'Your basket is not empty, received: {received_message}'

    def should_not_be_any_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
               "Basket isn't empty, but should be"
        
        
    
