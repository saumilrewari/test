import email
import imaplib
import time
import traceback

from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


# from opsis_project.base.base import BaseDriver


class Smoke_Test:
    def __init__(self, driver):
        self.driver = driver

    # self.base = BaseDriver(self.driver)

    def test_pass(self):
        try:
            print("You have entered into test_pass method")
            return True
        except Exception as e:
            print(e)
            return False

    def fetch_signin_Code(self):
        global code
        try:
            time.sleep(5)
            # USER = "infocusp123@gmail.com"
            # PASSWORD = "nzjfxnyxigcgdlux"
            USER = "infocusp123@gmail.com"
            PASSWORD = "kqsasbllftsuezid"
            imap_url = "imap.gmail.com"
            my_mail = imaplib.IMAP4_SSL(imap_url)
            my_mail.login(USER, PASSWORD)
            my_mail.select('Inbox')
            key = 'FROM'
            value = 'noreply@plateful.org'
            _, data = my_mail.search(None, key, value)
            mail_id_list = data[0].split()
            msgs = []
            count = 0

            for (num) in mail_id_list[::-1]:
                typ, data = my_mail.fetch(num, '(RFC822)')
                msgs.append(data)
                count = count + 1
                if count == 1:
                    break

            for msg in msgs[::-1]:
                for response in msg:
                    if type(response) is tuple:
                        my_msg = email.message_from_bytes((response[1]))
                        for part in my_msg.walk():
                            # print(part.get_content_type())
                            if part.get_content_type() == 'text/htlm':
                                body = (part.get_payload())
                                url = body.split("href=3D'")[1].split("'")[0]
            return url
        except Exception as e:
            print(str(e))

    def verify_launch_page(self):
        """
        This method will test all the items on launch page
        :return: boolean
        """
        # Launch Logo, Text, Scrolling images, start for free button.
        try:
            welcome = self.driver.find_element(By.XPATH, "//*[contains(@text, 'Welcome to')]")
            if welcome:
                print("\nWelcome note is present on the launch page")
            else:
                print("Welcome note is missing")
                return False

            launch_logo = self.driver.find_element(By.XPATH, '(//android.widget.ImageView[@content-desc="Logo"])[1]')
            if launch_logo:
                print("Logo is present on Launch page")
            else:
                print("Logo is missing")
                return False

            tagline = self.driver.find_element(By.XPATH, "//*[contains(@text, 'Healthy eating made easy.')]")
            if tagline:
                print("Tagline 'Healthy eating made easy.' is present on launch page")
            else:
                print("Tagline is missing")
                return False

            desc = self.driver.find_element(By.XPATH, "//*[contains(@text, 'Join the nutrition revolution, starting with FoodWise.')]")
            if desc:
                print("Description is present")
            else:
                print("Description is missing")
                return False

            scrollable_images = self.driver.find_element(By.XPATH, '(//android.widget.ImageView[@content-desc="Logo"])[2]')
            if scrollable_images:
                print("Image is present")
            else:
                print("Image is missing on the launch page")
                return False

            scroll = self.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]")
            if scroll:
                self.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]").click()
                self.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]").click()
                self.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[4]").click()
                self.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]").click()
                print("Scrolling option is present")
            else:
                print("Scrolling option is not present")
                return False

            start_button = self.driver.find_element(By.XPATH, '//*[@text = "Start For Free"]')
            if start_button:
                print("Start button is present on the launch page")
            else:
                print("Start button is missing")
                return False

            return True
        except Exception:
            print("Exception occurred in : verify_launch_page")
            return False

    def verify_login_page(self):
        """
        This method will verify all the items and functionality on Login page

        :return: boolean
        """
        try:
            if self.driver.find_element(By.XPATH, '//*[@text = "Start For Free"]'):
                self.driver.find_element(By.XPATH, '//*[@text = "Start For Free"]').click()
                time.sleep(2)
            else:
                print("you are not on start screen")
                return False

            login_logo = self.driver.find_element(By.XPATH, '(//android.widget.ImageView[@content-desc="Logo"])[1]')
            if login_logo:
                print("Logo is present on Login/SignUp Screen")
            else:
                print("Logo is missing on Login/SignUp Screen")

            signup_button = self.driver.find_element(By.XPATH, '//*[@text = "Sign Up"]')
            if signup_button:
                print("Signup button is present")
            else:
                print("Signup button is missing")

            login_button = self.driver.find_element(By.XPATH, '//*[@text = "Log In"]')
            if login_button:
                print("Login button is present")
            else:
                print("Login button is missing")

            return True
        except Exception:
            print("Exception occurred in : verify_login_page")
            return False

    def verify_signup_page(self):
        """
        This method verifies all the items ands functionality on signup page
        :return: boolean
        """
        try:

            signup_button = self.driver.find_element(By.XPATH, '//*[@text = "Sign Up"]')
            if signup_button:
                signup_button.click()
                time.sleep(2)
            signup_welcome = self.driver.find_element(By.XPATH, '//*[@text = "Welcome to Plateful!"]')
            if signup_welcome:
                print("Welcome note is present on signup screen")
            accept_agreement = self.driver.find_element(By.XPATH, "//android.widget.CheckBox[@content-desc='Agree to Terms of Use']")
            if accept_agreement:
                print("Accept Agreement checkbox is present")

            self.driver.find_element(By.XPATH, "//android.view.View[@content-desc='Go Back']").click()
            return True
        except Exception:
            print("Exception occurred in : verify_signup_page")
            return False

    def verify_confirm_email(self):
        """
        This method will perform login into application
        :return:
        """
        try:
            login_button = self.driver.find_element(By.XPATH, '//*[@text = "Log In"]')
            if login_button:
                login_button.click()
                print("Please provide valid email")
                time.sleep(20)
            else:
                print("login button is missing")
                return False

            permission = self.driver.find_element(By.XPATH, "//*[contains(@text, 'Permission request')]")
            if permission:
                permission.click()
                time.sleep(2)
                if self.driver.find_element(By.XPATH, "//*[contains(@text, 'While using the app')]"):
                    self.driver.find_element(By.XPATH, "//*[contains(@text, 'While using the app')]").click()
                    time.sleep(2)
                else:
                    print("Error occurred while giving permission to app")

            return True
        except Exception:
            print("Exception occurred in : verify_confirm_email")
            traceback.print_exc()
            return False


    def verify_start_button(self):
        """
        This method will check if user is on onboarding page, it will take the user in and give camera permissions.
        :return: boolean
        """
        try:
            if self.driver.find_element(By.XPATH, '//*[@text = "Start For Free"]'):
                self.driver.find_element(By.XPATH, '//*[@text = "Start For Free"]').click()
                time.sleep(2)
            else:
                print("you are not on start screen")

            permission = self.driver.find_element(By.XPATH, "//*[contains(@text, 'Permission request')]")
            if permission:
                permission.click()
                time.sleep(2)
                if self.driver.find_element(By.XPATH, "//*[contains(@text, 'While using the app')]"):
                    self.driver.find_element(By.XPATH, "//*[contains(@text, 'While using the app')]").click()
                    time.sleep(2)
                else:
                    print("Error occurred while giving permission to app")

            return True
        except Exception:
            print("Exception occurred in : verify_start_button")
            traceback.print_exc()
            return False

    def verify_barcode_page(self):
        """
        verify items and functionality on barcode reader page
        :return: boolean
        """
        try:
            self.verify_start_button()
            menu = self.driver.find_element(By.XPATH, "//android.widget.ImageView[@content-desc='Menu']")
            if menu:
                print("Three-dot menu is present")
                menu.click()
                time.sleep(2)
                if self.driver.find_element(By.XPATH, "//*[contains(@text, 'Intro Screens')]"):
                    print("Intro Screen is present")
                # if self.driver.find_element(By.XPATH, "//*[contains(@text, 'Account Information')]"):
                #     print("Acc Information option is present")
                # if self.driver.find_element(By.XPATH, "//*[contains(@text, 'Sign Out')]"):
                #     print("Sign-out option is present")
                self.driver.back()
                time.sleep(2)

            # if self.driver.find_element(By.XPATH, "//*[contains(@text, 'Scan Food Barcode')]"):
            #     print("Scan Barcode Title is present")
            # else:
            #     print("Scan Barcode Title is missing")
            #     return False

            if self.driver.find_element(By.XPATH, "(//android.widget.ImageView[@content-desc='Flash light on-off icon'])[1]"):
                print("Flashlight option is present")
            else:
                print("Flashlight option is missing")
                return False

            if self.driver.find_element(By.XPATH, "(//android.widget.ImageView[@content-desc='Flash light on-off icon'])[2]"):
                print("scan icon is present")
            else:
                print("scan icon is missing")

            if self.driver.find_element(By.XPATH, "//android.widget.ImageView[@content-desc='Scan history']"):
                print("scan history icon is present")
            else:
                print("scan history icon is missing")

            if self.driver.find_element(By.ID, "com.opsishealth.foodwise:id/zxing_viewfinder_view"):
                print("barcode viewfinder is present")
            else:
                print("barcode viewfinder is missing")

            return True
        except Exception:
            print("Exception occurred in : verify_barcode_page")
            return False







