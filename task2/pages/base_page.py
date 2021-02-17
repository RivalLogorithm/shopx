from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message="Can't find element by locator '{}'".format(locator))

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message="Can't find element by locator '{}'".format(locator))

    def find_element_in_list(self, list, id, locator, time=10):
        return WebDriverWait(list[id], time).until(EC.presence_of_element_located(locator),
                                               message="Can't find element by locator '{}'".format(locator))
    def switch_tab(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    def open(self):
        return self.driver.get(self.url)