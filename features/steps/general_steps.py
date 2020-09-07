from behave import given
from features.helper.browser_helper import BrowserSupport, BrowserType


@given("The user is on the Home Page")
def check_home_page(context):
    browser = BrowserSupport(url="https://aotjiratests.atlassian.net")
    browser.launch_browser(BrowserType.FIREFOX)
    context.browser = browser

