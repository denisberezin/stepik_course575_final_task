from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_the_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def get_product_cost(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_total_basket_cost(self):
        return self.browser.find_element(*ProductPageLocators.TOTAL_BASKET_COST_AFTER_ADDING).text

    def get_added_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_AFTER_ADDING).text

    def should_be_correct_product_name(self, product_name):
        added_product_name = self.get_added_product_name()
        assert added_product_name == product_name, f'Expected product name is "{product_name}" but "{added_product_name}" was added.'
        
    def should_be_correct_total_basket_cost(self, product_cost):
        total_basket_cost = self.get_total_basket_cost()
        assert total_basket_cost == product_cost, f'Expected basket cost = {product_cost} but {total_basket_cost} was shown.'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
               "Success message is presented, but should not be"

    def should_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
               "Success message isn't disappeared, but should be"


        
        
