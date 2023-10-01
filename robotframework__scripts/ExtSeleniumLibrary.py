from SeleniumLibrary import SeleniumLibrary
from SeleniumLibrary.base import keyword
import selenium


class ExtSeleniumLibrary(SeleniumLibrary):

    @keyword('OPEN CHROME WITH DOWNLOAD')
    def open_chrome_browser(self, url):
        options = selenium.webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-web-security")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--safebrowsing-disable-extension-blacklist")
        options.add_argument("--safebrowsing-disable-download-protection")
        prefs = {'safebrowsing.enabled': 'true'}
        options.add_experimental_option("prefs", prefs)
        instance = self.create_webdriver('Chrome', desired_capabilities=options.to_capabilities())
        self.go_to(url)