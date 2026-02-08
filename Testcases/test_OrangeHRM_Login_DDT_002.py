import time


import allure
import pytest

from Page_Objects.Login_page import Login_Page_class
from Utilities import readConfig
from Utilities.XLUtils import Excel_methods
from Utilities.logger import log_generator_class
from Utilities.readConfig import ReadConfig


@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_Login_DDT_002:
    driver=None
    username=ReadConfig.get_username()
    password=ReadConfig.get_password()
    login_url=ReadConfig.get_login_url()

    log=log_generator_class.log_gen_method()
    excel_path=".\\Testdata\\OrangeHRM_ExcelData.xlsx"
    sheet_name="Sheet1"


    def test_OrangeHRM_Login_DDT_003(self):
         #self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
         #Read data from ReadConfig file

         self.driver.get(self.login_url)
         self.log.info("OrangeHRM Login Page Opened")
         self.row_count=Excel_methods.count_rows(self.excel_path,self.sheet_name)
         self.log.info(f"Number of rows is excel file {self.row_count}")

         result_list=[]
         for i in range(2,self.row_count+1):
             self.driver.get(self.login_url)
             self.log.info(f"Opening Browser and getting {self.login_url}")
             username=Excel_methods.read_data_from_excel_file(self.excel_path,self.sheet_name,i,2)
             password=Excel_methods.read_data_from_excel_file(self.excel_path,self.sheet_name,i,3)
             self.expected_result=Excel_methods.read_data_from_excel_file(self.excel_path,self.sheet_name,i,4)
             login = Login_Page_class(self.driver)
             self.log.info(f"Entering username {self.username}")
             login.Enter_username(username)
             self.log.info(f"Entering username {self.password}")
             login.Enter_password(password)
             self.log.info(f"Clicking on login button")
             login.Login_button_click()

             if login.verify_login()=="Login Successful":
                 self.log.info(f"Login Successful for Username={username}")
                 self.driver.save_screenshot(f"Screenshots\\test_OrangeHRM_Login_DDT_003_pass_{username}.png")
                 allure.attach.file(f"Screenshots\\test_OrangeHRM_Login_DDT_003_pass_{username}.png",
                                    name=f"test_OrangeHRM_Login_DDT_003_pass_{username}",
                                    attachment_type=allure.attachment_type.PNG)

                 login.menu_button_click()
                 login.logout_button_click()
                 actual_result = "login pass"
                 Excel_methods.write_data_to_excel_file(self.excel_path, self.sheet_name, i, 5, actual_result)

             else:
                 self.log.info(f"Login unsuccessful for Username={username}")
                 self.driver.save_screenshot(f"Screenshots\\test_OrangeHRM_Login_DDT_003_pass_{username}.png")
                 allure.attach.file(f"Screenshots\\test_OrangeHRM_Login_DDT_003_pass_{username}.png",
                                    name=f"test_OrangeHRM_Login_DDT_003_pass_{username}",
                                    attachment_type=allure.attachment_type.PNG)
                 actual_result = "login fail"
                 Excel_methods.write_data_to_excel_file(self.excel_path,self.sheet_name,i,5,actual_result)

             if self.expected_result==actual_result:
              self.Test_status="Pass"
              Excel_methods.write_data_to_excel_file(self.excel_path,self.sheet_name,i,6,self.Test_status)
             else:
                 self.Test_status = "Fail"
                 Excel_methods.write_data_to_excel_file(self.excel_path, self.sheet_name, i, 6, self.Test_status)

             result_list.append(self.Test_status)
             if "Fail" not in result_list:
                self.log.info("All test cases passed")
             else:
                self.log.info("All test cases failed")
                assert False

         self.log.info("All test cases completed")

















#pytest -v -n=auto --html=HTML_Reports\OrangeHRM_report.html --alluredir=AllureReports  --browser=edge