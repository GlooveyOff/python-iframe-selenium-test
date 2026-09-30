from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.second_frame import SecondFrame


class MainPage(BasePage):
    SECOND_FRAME = (By.ID, "iframe-2")

    def __init__(self, driver):
        super().__init__(driver)
        self.second_frame = SecondFrame(driver)

    def get_python_stable_download_link(self):
        self.switch_to_frame(self.SECOND_FRAME)
        try:
            self.second_frame.open_downloads()
            return self.second_frame.get_python_stable_link()
        finally:
            self.switch_to_default_content()
