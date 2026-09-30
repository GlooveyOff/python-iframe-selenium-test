from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SecondFrame(BasePage):
    DOWNLOADS = (By.CSS_SELECTOR, "a.nav-link[href$='/downloads']")
    PYTHON_STABLE_LINK = (
        By.XPATH,
        "//p[normalize-space()='Python']"
        "/following-sibling::p[starts-with(normalize-space(), 'Stable:')]/a",
    )

    def open_downloads(self):
        self.click(self.DOWNLOADS)

    def get_python_stable_link(self):
        return self.get_attribute(self.PYTHON_STABLE_LINK, "href")
