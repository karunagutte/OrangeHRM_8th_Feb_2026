import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class")
def driver_setup(request):
    browser=request.config.getoption("--browser")
    if browser=="firefox":
        print("\nOpening Firefox Browser")
        driver=webdriver.Firefox()
    elif browser=="chrome":
        print("\nOpening Chrome Browser")
        driver=webdriver.Chrome()
    elif browser=="edge":
        print("\nOpening Edge Browser")
        driver=webdriver.Edge()
    elif browser=="headless":
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver=webdriver.Chrome(options=chrome_options)
    else:
        print("Invalid Browser")
        driver=None

    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver=driver

    yield driver
    print("\n Browser Closed")
    driver.quit()




