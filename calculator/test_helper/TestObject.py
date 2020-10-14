import selenium.webdriver as webdriver
import calculator.config as config


class TestObject:
    """
    Driver initialization, opening website on browser
    """
    def __init__(self):
        print("## Checking on calculator ##")
        self.driver = webdriver.Chrome(config.chrome_driver)

    def start(self):
        _delay = 10
        self.driver.maximize_window()
        self.driver.get(config.web)
        self.driver.implicitly_wait(10)

        return self.driver
