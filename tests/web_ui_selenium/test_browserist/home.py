from browserist import Browser
from guara.transaction import AbstractTransaction


class SubmitText(AbstractTransaction):
    """
    Submits the text

    Args:
        text (str): The text to be submited

    Returns:
        str: the label 'It works! {code}!'
    """

    def __init__(self, driver):
        super().__init__(driver)
        self._driver: Browser

    def do(self, text):
        TEXT = '//*[@id="input"]'
        BUTTON_TEST = '//*[@id="button"]'
        RESULT = '//*[@id="result"]'
        self._driver.input.value(TEXT, text)
        self._driver.click.button(BUTTON_TEST)
        return self._driver.get.text(RESULT)