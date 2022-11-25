
class BaseUIApp:
    """
    This class stands for connecting abstract methods with a selenium tool
    """

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_element(self, locator_type, locator_value):
        return self.driver.find_element(locator_type, locator_value)

    def click(self, locator_type, locator_value):
        el = self.get_element(locator_type, locator_value)
        el.click()

    def enter_text(self, locator_type, locator_value, text):
        el = self.get_element(locator_type, locator_value)
        el.send_keys(text)

    def open_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
