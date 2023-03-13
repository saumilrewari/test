from appium import webdriver
desired_caps = {
  "platformName": "iOS",
  "appium:platformVersion": "16.0.2",
  "appium:deviceName": "iPhone 11",
  "appium:automationName": "XCUITest",
  "appium:udid":"00008110-001E545C0C44401E",
  # "appium:udid": "D3EE9932-5E4F-419C-B516-E0FBF05B5474",
  "appium:app": "/Users/mehulthakkar/Downloads/FoodWise.app",
  # "appium:app": "/Users/mehulthakkar/Library/Developer/Xcode/DerivedData/WebDriverAgent-aghlrsejdreqngftgvcqwnjgrbou/Build/Products/Debug-iphonesimulator/IntegrationApp.app"
  "appium:bundleId": "com.opsishealth.foodwise.dev",
  # "appium:xcodeOrgId": "QHY4BJKPUM",
  "appium:xcodeOrgId": "H6DHG2JDDT",
  "appium:xcodeSigningId": "iPhone Developer"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.start_client()
print("driver initiated successfully")
