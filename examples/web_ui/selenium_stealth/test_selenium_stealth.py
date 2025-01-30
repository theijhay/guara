from guara.transaction import Application
from guara import it
from examples.web_ui.selenium_stealth.setup import OpenStealthBrowser, CloseStealthBrowser
from examples.web_ui.selenium_stealth.home import HomeTransactions
from random import randrange
from selenium import webdriver


class TestSeleniumStealthIntegration:
    """
    TestSeleniumStealthIntegration is a test class for integrating
    Selenium Stealth with a local web page.
    """

    def setup_method(self, method):

        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--headless")

        driver = webdriver.Chrome(options=options)
        self._app = Application(driver)
        self._app.at(OpenStealthBrowser)

    def teardown_method(self, method):
        self._app.at(CloseStealthBrowser)

    def test_local_page(self):
        text = ["cheese", "selenium", "test", "bla", "foo"]
        text = text[randrange(len(text))]
        self._app.at(HomeTransactions, text=text).asserts(
            it.Contains, "Example Domain"
        )
        self._app.at(HomeTransactions, text=text).asserts(it.IsNotEqualTo, "Any")
