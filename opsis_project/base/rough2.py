import email
import imaplib
import time
from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {
    "platformName": "Android",
    "deviceName": "RZ8T50P0JAT",
    "automationName": "UiAutomator2",
    "appPackage": "com.opsishealth.foodwise",
    "appWaitActivity": "com.opsis.primary.MainActivity",
    "app": "/Users/mehulthakkar/Downloads/opsis_debug.apk"
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.start_client()
time.sleep(3)

# click start button
start_button = driver.find_element(By.XPATH, '//*[@text = "Start For Free"]')
if start_button:
    print("Start button is present")
    time.sleep(2)
    start_button.click()

login_button = driver.find_element(By.XPATH, '//*[@text = "Log In"]')
if login_button:
    print("Login button is present")
    login_button.click()

email_textbox = driver.find_element(By.XPATH, '//android.view.View[@content-desc="Email"]')
email_textbox.click()
email_textbox.clear()
e = driver.find_element(By.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.EditText/android.view.View[2]/android.view.View')
e.click()
e.clear()
# e.send_keys("infocusp123@gmail.com")
time.sleep(15)  # manually enter Email

signin_button = driver.find_element(By.XPATH, '//android.view.View[@content-desc="Sign In Button"]')
signin_button.click()

# confirm your email
email_text = driver.find_element(By.XPATH, "//*[contains(@text, 'confirm your email address')]")
if email_text:
    driver.start_activity("com.google.android.gm", "ConversationListActivityGmail")
    print(driver.current_package)
    no_reply = driver.find_element(By.XPATH, "//*[contains(@text, 'noreply')]")
    if no_reply:
        no_reply.click()
        print("I have entered email from noreply")
        show_text = driver.find_element(By.XPATH, "//*[contains(@text, 'Show quoted text')]")
        if show_text:
            show_text.click()

# after login give permission
permission = driver.find_element(By.XPATH, "//*[contains(@text, 'Permission request')]")
if permission:
    permission.click()
    driver.find_element(By.XPATH, "//*[contains(@text, 'While using the app')]")

# verify things on barcode reader page
# 1. Three-dot Menu
menu = driver.find_element(By.XPATH, "//android.widget.ImageView[@content-desc='Menu']")
if menu:
    print("Three-dot menu is present")
    menu.click()
    assert driver.find_element(By.XPATH, "//*[contains(@text, 'Intro Screens')]")
    assert driver.find_element(By.XPATH, "//*[contains(@text, 'Account Information')]")
    assert driver.find_element(By.XPATH, "//*[contains(@text, 'Sign Out')]")
    menu.click()
# Scan Barcode title
assert driver.find_element(By.XPATH, "//*[contains(@text, 'Scan Barcode')]")

# Flashlight option
assert driver.find_element(By.XPATH, "//android.widget.ImageView[@content-desc='Flash light on-off icon']")

#barcode view finder
assert driver.find_element(By.ID, "com.opsishealth.foodwise:id/zxing_viewfinder_view")
