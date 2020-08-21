from selenium import webdriver


class BasePage:
    url = ''

    def __init__(self, reuse):
        self.driver = ''
        if reuse:
            chrome_opts = webdriver.ChromeOptions()
            chrome_opts.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=chrome_opts)
            self.driver.maximize_window()
            self.driver.implicitly_wait(3)
        else:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            if self.url:
                self.driver.get(self.url)
            self.driver.implicitly_wait(3)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)
