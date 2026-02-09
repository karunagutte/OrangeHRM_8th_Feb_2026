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
    # new_username=ReadConfig.get_new_username()
    # new_password=ReadConfig.get_new_password()
    # confirm_password=ReadConfig.get_confirm_password()
    # employee_name=ReadConfig.get_employee_name()
    firstname=ReadConfig.get_firstname()
    middle_name=ReadConfig.get_middle_name()
    lastname=ReadConfig.get_lastname()
    path=ReadConfig.get_image()

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


    def test_add_Employee(self):
        self.log.info("Checking Login page")
        self.driver.get(self.login_url)

        login_page = Login_Page_class(self.driver)
        # login_page.Enter_password("Admin")
        self.log.info("Entering username")
        login_page.Enter_username(self.username)

        # login_page.Enter_password("admin123")
        self.log.info("Entering password")
        login_page.Enter_password(self.password)
        login_page.Login_button_click()

        #Add Employee

        login_page.click_pim()
        self.log.info("PIM page is opened")
        login_page.add_employee()
        self.log.info("Add Employee page is opened")
        login_page.upload_image(self.path)
        self.log.info("Image Upload is opened")
        login_page.Enter_first_name(self.firstname)
        self.log.info("Firstname entered")
        login_page.Enter_middle_name(self.middle_name)
        self.log.info("middle_name entered")
        login_page.Enter_last_name(self.lastname)
        self.log.info("lastname entered")
        time.sleep(10)
        self.driver.save_screenshot("Screenshots\\test_add_employee.png")
        login_page.save_employee()



    # def test_OrangeHRM_Add_user_004(self):
         #         self.log.info("Adding new user")
         #         self.driver.get(self.login_url)
         #         login_page = Login_Page_class(self.driver)
    #         login_page.Enter_username(self.username)
    #         login_page.Enter_password(self.password)
    #         login_page.Login_button_click()
    #
    #         #Add user
    #         login_page.click_admin()
    #         self.log.info("Admin Page Opened")
    #         login_page.click_add_user()
    #         self.log.info("Add user page Opened")
    #         login_page.select_user_role()
    #         self.log.info("Selected user role")
    #         login_page.enter_employee_name(self.employee_name)
    #         self.log.info("Enter employee_name")
    #         login_page.select_status()
    #         self.log.info("select status")
    #         login_page.enter_username(self.new_username)
    #         self.log.info("username entered")
    #         login_page.Enter_password(self.new_password)
    #         self.log.info("password entered")
    #         login_page.confirm_Password(self.confirm_password)
    #         self.log.info("confirm password entered")
    #
    #         self.driver.save_screenshot("Screenshots\\new_user.png")
    #         login_page.click_save()
    #         login_page.menu_button_click()
    #         login_page.logout_button_click()










#pytest -v -n=auto --html=HTML_Reports\OrangeHRM_report.html --alluredir=AllureReports  --browser=edge