from guara.transaction import AbstractTransaction
from caqui import synchronous


class OpenApp(AbstractTransaction):
    """
    Opens the App

    Args:
        session (object): The session of the Web Driver
        driver_url (str): The URL to connect the Web Driver server
        page_url (str): The URL of the App

    Returns:
        str: the title of the App
    """

    def __init__(self, driver):
        super().__init__(driver)

    def do(self, with_session, connect_to_driver, access_url):
        synchronous.go_to_page(
            connect_to_driver,
            with_session,
            access_url,
        )
        return synchronous.get_title(connect_to_driver, with_session)


class CloseApp(AbstractTransaction):
    """
    Opens the App

    Args:
        with_session (object): The session of the Web Driver
        connect_to_driver (str): The URL to connect the Web Driver server
        page_url (str): The URL of the App

    Returns:
        str: the title of the App
    """

    def __init__(self, driver):
        super().__init__(driver)

    def do(self, with_session, connect_to_driver):
        synchronous.take_screenshot(connect_to_driver, with_session, "./captures/")
        synchronous.close_session(connect_to_driver, with_session)