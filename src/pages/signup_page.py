from src.config.config import config


class SigupPage:
    PAGE_URL = '/signup'

    def __init__(self, ui_app) -> None:
        self.ui_app = ui_app

    def goto_page(self):
        self.ui_app.open_page(config.BASE_URL_UI + self.PAGE_URL)
