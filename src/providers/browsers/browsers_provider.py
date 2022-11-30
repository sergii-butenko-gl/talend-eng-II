from src.providers.browsers.library.edge_browser import EdgeBrowser
from src.providers.browsers.library.chrome_browser import ChromeBrowser
from src.providers.browsers.library.firefox_browser import FirefoxBrowser
from src.providers.browsers.library.remote_chrome_browser import RemoteChromeBrowser


class BrowserProvider:
    MAPPER = {
        'chrome': ChromeBrowser,
        'firefox': FirefoxBrowser,
        'edge': EdgeBrowser,
        'remote_chrome': RemoteChromeBrowser,
    }

    @classmethod
    def get_driver(cls, browser_name: str):
        browser_class = cls.MAPPER.get(browser_name)
        if browser_class is None:
            print("ERROR - Browser is not registered in the framework. Please register it first")

        return browser_class.get_driver()
