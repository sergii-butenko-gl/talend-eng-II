from src.applications.base_ui_app import BaseUIApp
from src.config.config import config
import time
from selenium.webdriver.common.by import By


class GitHubUI(BaseUIApp):
    # 
    # driver.get(config.BASE_URL_UI)

    def __init__(self) -> None:
        super().__init__()
        pass

    def open_base_page(self):
        self.open_page(config.BASE_URL_UI)

    def goto_login_page(self):
        self.open_page(config.BASE_URL_UI + '/login')

    def login(self, username, password):
        self.enter_text(By.ID, 'login_field', username)
        self.enter_text(By.ID, 'password', password)
        self.click(By.NAME, 'commit')

        time.sleep(5)


    def logout(self):
        pass
    
    def check_title(self):
        pass
