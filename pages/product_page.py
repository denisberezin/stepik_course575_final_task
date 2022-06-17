from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_the_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    #def check_total_basket_cost(self):

    def get_product_cost(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_total_basket_cost(self):
        return self.browser.find_element(*ProductPageLocators.TOTAL_BASKET_COST_AFTER_ADDING).text

    def get_added_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_AFTER_ADDING).text


        
        