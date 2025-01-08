from playwright.sync_api import Page
from guara.transaction import AbstractTransaction


class NavigateToGettingStarted(AbstractTransaction):
    """
    Navigates to Getting Started page

    Returns:
        str: the heading 'Installation'
    """

    def __init__(self, driver):
        super().__init__(driver)
        self._driver: Page

    def do(self, **kwargs):
        self._driver.get_by_role("link", name="Get started").click()
        return self._driver.get_by_role("heading", name="Installation").text_content()