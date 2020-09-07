from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from features.pages.base_page import BasePage
from features.helper.locator_helper import ByHelper as by, LocatorHelper as locator


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    _username_txt = locator.element("username", by.ID)
    _password_txt = locator.element("password", by.ID)
    _login_button = locator.element("login-submit", by.ID)

    def set_username(self, username):
        print("_username: ", self._username_txt)
        username_element = self.find_element(self._username_txt)
        username_element.clear()
        username_element.send_keys(username)

    def set_password(self, password):
        password_element = self.wait_for_element_clickable(self._password_txt, 8)
        password_element.clear()
        password_element.send_keys(password)

    def continue_action(self):
        continue_element = self.wait_for_element_clickable(self._login_button)
        continue_element.click()

