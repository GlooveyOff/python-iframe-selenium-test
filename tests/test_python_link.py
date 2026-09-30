from pages.main_page import MainPage


EXPECTED_PYTHON_LINK = "https://pypi.python.org/pypi/selenium"


def test_python_download_link(driver, url):
    main_page = MainPage(driver)
    main_page.open(url)

    python_link = main_page.get_python_stable_download_link()

    assert python_link == EXPECTED_PYTHON_LINK
