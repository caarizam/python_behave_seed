from behave import given, when, then, step
import logging as logger
from features.pages.home_page import HomePage
from features.pages.welcome_page import WelcomePage


@when("The user requests for login with username {username} and password {password}")
def user_login_action(context, username, password):

    if username is None or password is None:
        raise Exception("Username and password can not be empty")
    context.username = username
    home = HomePage(context.browser.driver)
    home.set_username(username)
    home.continue_action()
    home.set_password(password)
    home.continue_action()


@then("The user should see the Welcome Page")
def check_welcome_page(context):
    welcome = WelcomePage(context.browser.driver)
    welcome.is_welcome_page()
    welcome.select_project("automation")