from src.pages.forgot_password_page import ForgorPasswordPage
from src.config.config import config
from selenium.webdriver.common.by import By


class LoginPage:
    PAGE_URL = '/login'

    username_field = (By.ID, 'login_field')
    password_field = (By.ID, 'password')
    sign_in_button = (By.NAME, 'commit')
    forgot_password_link = (By.PARTIAL_LINK_TEXT, 'Forgot password')
    # else elements

    def __init__(self, ui_app) -> None:
        self.ui_app = ui_app

    def login(self, username, password):
        self.goto_page()
        self.ui_app.enter_text(self.username_field, username)
        self.ui_app.enter_text(self.password_field, password)
        self.ui_app.click(self.sign_in_button)

    def goto_page(self):
        self.ui_app.open_page(config.BASE_URL_UI + self.PAGE_URL)

    def forgot_password(self):
        self.ui_app.click(self.forgot_password_link)
        return ForgorPasswordPage(self.ui_app)