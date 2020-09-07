from selenium.webdriver.common.by import By
from enum import Enum


class ByHelper(Enum):

    ID = By.ID
    NAME = By.NAME
    CLASS = By.CLASS_NAME
    CSS_SELECTOR = By.CSS_SELECTOR
    LINK_TEXT = By.LINK_TEXT
    PARTIAL_LINK_TEXT = By.PARTIAL_LINK_TEXT
    TAG_NAME = By.TAG_NAME
    XPATH = By.XPATH


class LocatorHelper:

    @staticmethod
    def element(value: str, _type: ByHelper):
        return {
            "by": _type,
            "value": value

        }
