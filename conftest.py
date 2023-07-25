from selenium import webdriver
import pytest


# Session Setup/Teardown
@pytest.fixture(scope='session')
def setup():
    print("\nSuite setup! Launching browser..")
    driver = launch_edge()
    yield
    print("\n..Suite teardown, closing browser.")
    driver.quit()


@pytest.fixture(params=['chrome', 'edge', 'firefox'])
def initialize_driver(request):
    print("\nSuite setup! Launching browser..")
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'edge':
        driver = webdriver.Edge()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()

    request.cls.driver = driver
    print("Browser: ", request.param)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield
    print('\n..Suite teardown, closing browser.')
    driver.close()


def launch_chrome():
    print('launching chrome..')
    chr_options = webdriver.ChromeOptions()
    # Prevents browser closing after method finishes execution
    chr_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chr_options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    return driver


def launch_edge():
    print('launching edge..')
    edge_options = webdriver.EdgeOptions()
    # Currently empty - no options added

    driver = webdriver.Edge(options=edge_options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    return driver


def launch_firefox():
    print('launching firefox..')
    fire_options = webdriver.FirefoxOptions()
    # Currently empty - no options added

    driver = webdriver.Firefox(options=fire_options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    return driver
