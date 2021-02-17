from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AvitoSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.NAME, 'login')
    LOCATOR_PASSWORD_FIELD = (By.NAME, 'password')
    LOCATOR_AUTH_BUTTON = (By.NAME, 'submit')
    LOCATOR_AUTH_ERROR = (By.XPATH, "//p[contains(@class, 'form-error-24xMu')]")
    LOCATOR_PROFILE = (By.XPATH, "//a[@href='/profile']")
    LOCATOR_ITEMS_LIST = (By.XPATH, "//div[@data-marker='item']")
    LOCATOR_ITEM = (By.XPATH, ".//h3[@itemprop='name']")
    LOCATOR_DELIVERY_BUTTON = (By.XPATH, "//button[@data-marker='delivery-item-button-main']")
    LOCATOR_PHONE_FIELD = (By.XPATH, "//input[@data-marker='sd/order-widget-field/phone']")


class MainPage(BasePage):
    def enter_login_and_pass(self,_login, _password):
        login = self.find_element(AvitoSearchLocators.LOCATOR_LOGIN_FIELD)
        login.send_keys('{}'.format(_login))

        password = self.find_element(AvitoSearchLocators.LOCATOR_PASSWORD_FIELD)
        password.send_keys('{}'.format(_password))

    def click_submit_button(self):
        self.find_element(AvitoSearchLocators.LOCATOR_AUTH_BUTTON).click()

    def is_login_in(self):
        profile = self.find_element(AvitoSearchLocators.LOCATOR_PROFILE, time=60)
        return profile.text

    def get_item(self, item_id):
        items = self.find_elements(AvitoSearchLocators.LOCATOR_ITEMS_LIST)
        self.find_element_in_list(items, item_id, AvitoSearchLocators.LOCATOR_ITEM).click()

    def select_new_tab(self):
        self.switch_tab()

    def click_delivery_button(self):
        self.find_element(AvitoSearchLocators.LOCATOR_DELIVERY_BUTTON).click()

    def get_phone_field(self):
        phone = self.find_element(AvitoSearchLocators.LOCATOR_PHONE_FIELD).get_attribute(
            'value')
        return phone
