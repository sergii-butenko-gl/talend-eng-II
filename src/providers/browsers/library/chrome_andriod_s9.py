from src.providers.browsers.library.base_browser_class import BaseBrowserClass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class ChromeAndroidS9Device(BaseBrowserClass):
    OPTIONS = {'size': 100 * 100}

    @classmethod
    def get_driver(cls):
        service_obj = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service_obj, options=cls.OPTIONS)
