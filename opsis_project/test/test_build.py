import pytest
from opsis_project.page.smoke_test import Smoke_Test


@pytest.mark.usefixtures("setup")
class Test_Build:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        """
        Creating the object and passing appium webdriver instance into it, var_name = driver
        :return: none
        """
        self.smoketest = Smoke_Test(self.driver)

    def test_pass(self):
        """This test will verify the elements and functionality present on the launch page"""
        assert self.smoketest.test_pass()

    def test_verify_launch_page(self):
        """This test will verify the elements and functionality present on the launch page"""
        assert self.smoketest.verify_launch_page()

    def test_verify_barcode_page(self):
        """This test will verify the elements and functionality present on the barcode page"""
        assert self.smoketest.verify_barcode_page()

    # def test_verify_login_page(self):
    #     """This test will verify the elements and functionality present on the login page"""
    #     assert self.smoketest.verify_login_page()
    #
    # def test_verify_signup_page(self):
    #     """This test will verify the elements and functionality present on the signup page"""
    #     assert self.smoketest.verify_signup_page()
    #
    # def test_verify_confirm_email(self):
    #     """This test will verify the elements and functionality present while performing email confirmation"""
    #     assert self.smoketest.verify_confirm_email()
