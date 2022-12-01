
class BaseUIApp:
    """
    This class stands for connecting abstract methods with a selenium tool
    """

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        el = self.get_element(locator)
        el.click()

    def enter_text(self, locator, text):
        el = self.get_element(locator)
        el.send_keys(text)

    def open_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def get_title(self):
        return self.driver.title

    def close(self):
        self.driver.quit()
