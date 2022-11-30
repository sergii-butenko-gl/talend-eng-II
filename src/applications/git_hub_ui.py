from src.pages.forgot_password_page import ForgorPasswordPage
from src.pages.signup_page import SigupPage
from src.pages.login_in_page import LoginPage
from src.applications.base_ui_app import BaseUIApp
from src.config.config import config


class GitHubUI(BaseUIApp):
    
    def __init__(self, driver) -> None:
        super().__init__(driver=driver)
        self.login_page = LoginPage(self)
        self.signup_page = SigupPage(self)
        self.forgot_password_page = ForgorPasswordPage(self)
        self.header_compoments = "ksjdabfkjbasdkjfn"

    def open_base_page(self):
        self.open_page(config.BASE_URL_UI)

    def logout(self):
        self.click(self.logout_button)
