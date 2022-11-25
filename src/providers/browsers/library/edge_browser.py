from src.providers.browsers.library.base_browser_class import BaseBrowserClass
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class EdgeBrowser(BaseBrowserClass):
    OPTIONS = None

    @classmethod
    def get_driver(cls):
        service_obj = Service(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=service_obj, options=cls.OPTIONS)
