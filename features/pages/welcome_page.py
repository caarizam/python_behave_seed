from features.helper.locator_helper import ByHelper as by, LocatorHelper as locator
from features.pages.base_page import BasePage


class WelcomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    _projects_label = locator.element(".styled__StyledTitle-sc-1a16ki5-1", by.CSS_SELECTOR)

    def is_welcome_page(self):
        welcome_label = self.wait_for_element_visible(self._projects_label, 30)

    def select_project(self, name):
        _project_name = locator.element(name, by.LINK_TEXT)
        project_link = self.wait_for_element_clickable(_project_name, 25)
        project_link.click()
