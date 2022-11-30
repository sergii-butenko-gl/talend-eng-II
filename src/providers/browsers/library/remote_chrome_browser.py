from src.config.config import config
from src.providers.browsers.library.base_browser_class import BaseBrowserClass
from selenium import webdriver


class RemoteChromeBrowser(BaseBrowserClass):
    OPTIONS = None

    @classmethod
    def get_driver(cls):
        driver = webdriver.Remote(
            command_executor=config.SELENIUM_GRID_URL,
            desired_capabilities={
                "browserName": "chrome",
            },
        )

        return driver
