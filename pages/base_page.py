
class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """This method opens a browser by the provided link"""
        self.browser.get(self.url)
