import time
import pytest
from appium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    # Launch Appium Driver
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        # "deviceName": "RZ8T50P0JAT", # Blue phone
        # "deviceName": "R9PT60K71VA", # Tab
        "automationName": "UiAutomator2",
        "appPackage": "com.opsishealth.platefuldev",
        "appWaitActivity": "com.opsis.primary.MainActivity",
        "app": "/Users/saumilrewari/PycharmProjects/Opsis/opsis_project/base/plateful_dev.apk"
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.start_client()

    time.sleep(10)

    # base_driver = BaseDriver(driver)
    request.cls.driver = driver

    yield
    driver.quit()
