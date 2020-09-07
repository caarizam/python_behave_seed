from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, driver: webdriver):
        self.driver = driver

    def wait_for_element_clickable(self, element, seconds=10):
        print("value_identifier: ", element["value"])
        wait = WebDriverWait(self.driver, seconds)
        element_expected = wait.until(EC.element_to_be_clickable((element["by"].value, element["value"])))
        return element_expected

    def wait_for_element_visible(self, element, seconds=10):
        print("value_identifier: ", element["value"])
        wait = WebDriverWait(self.driver, seconds)
        element_expected = wait.until(EC.visibility_of_element_located((element["by"].value, element["value"])))
        return element_expected

    def wait_for_element_enabled(self, element, seconds=10):
        print("value_identifier: ", element["value"])
        wait = WebDriverWait(self.driver, seconds)
        element_expected = wait.until(EC.presence_of_element_located(( element["by"].value, element["value"])))

    def move_mouse_action(self, driver, element):
        action = ActionChains(driver)
        action.move_to_element(element)
        action.perform()

    def find_element(self, element):
        return self.driver.find_element(element['by'].value, element['value'])