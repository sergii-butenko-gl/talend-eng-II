from src.providers.browsers.library.base_browser_class import BaseBrowserClass
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class FirefoxBrowser(BaseBrowserClass):
    OPTIONS = None

    @classmethod
    def get_driver(cls):
        service_obj = Service(GeckoDriverManager().install())
        return webdriver.Firefox(service=service_obj, options=cls.OPTIONS)
