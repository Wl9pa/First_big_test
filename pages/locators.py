from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#id_login-redirect_url")
    LOGIN_REGISTER = (By.CSS_SELECTOR, "#id_registration-redirect_url")
