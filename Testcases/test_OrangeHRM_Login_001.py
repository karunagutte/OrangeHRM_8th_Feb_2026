import time


import allure
import pytest

from Page_Objects.Login_page import Login_Page_class
from Utilities import readConfig
from Utilities.logger import log_generator_class
from Utilities.readConfig import ReadConfig


@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_Login_001:
    driver=None
    username=ReadConfig.get_username()
    password=ReadConfig.get_password()
    login_url=ReadConfig.get_login_url()

    log=log_generator_class.log_gen_method()


    @pytest.mark.falky(rerun=1)
    @allure.title("Verify OrangeHRM Title")
    @allure.story("Verify OrangeHRM Title")
    @pytest.mark.sanity
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_verify_OrangeHRM_url_001(self):
     #self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
     self.log.info("Verify OrangeHRM Title")
     self.driver.get(self.login_url)
     if self.driver.title == "OrangeHRM":
         time.sleep(5)
         self.log.info("Taking screenshot")
         self.driver.save_screenshot("Screenshots\\test_verify_url_pass.png")
         allure.attach.file("Screenshots\\test_verify_url_pass.png")
     else:
         time.sleep(5)
         self.log.info("Taking screenshot")
         self.driver.save_screenshot("Screenshots\\test_verify_url_fail.png")
         allure.attach.file("Screenshots\\test_verify_url_fail.png")
         assert False

     self.log.info("Login Test Completed")

    @allure.title("Verify OrangeHRM Title")
    @allure.story("Verify OrangeHRM Title")
    @allure.tag("tag")
    @allure.description("Verify OrangeHRM Title")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    @pytest.mark.smoke
    @pytest.mark.falky(rerun=1)
    def test_OrangeHRM_Login_002(self):
         #self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
         #Read data from ReadConfig file
         self.log.info("Checking Login page")
         self.driver.get(self.login_url)

         login_page=Login_Page_class(self.driver)
         #login_page.Enter_password("Admin")
         self.log.info("Entering username")
         login_page.Enter_username(self.username)

         #login_page.Enter_password("admin123")
         self.log.info("Entering password")
         login_page.Enter_password(self.password)
         login_page.Login_button_click()
         if login_page.verify_login()=="Login Successful":

             time.sleep(10)

             self.driver.save_screenshot("Screenshots\\test_login_successful.png")
             allure.attach.file("Screenshots\\test_login_successful.png")
             login_page.menu_button_click()
             login_page.logout_button_click()
             assert True
         else:
             time.sleep(10)
             self.log.error("Login Not successful")
             self.driver.save_screenshot("Screenshots\\test_login_unsuccessful.png")
             allure.attach.file("Screenshots\\test_login_unsuccessful.png")
             assert False

         self.log.info("Login Test Completed")








#pytest -v -n=auto --html=HTML_Reports\OrangeHRM_report.html --alluredir=AllureReports  --browser=edge