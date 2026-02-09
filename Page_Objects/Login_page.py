import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Login_Page_class:
  text_username_xpath="//input[@placeholder='Username']"
  text_password_xpath="//input[@placeholder='Password']"
  login_button_xpath="//button[@type='submit']"
  menu_button_xpath="//p[@class='oxd-userdropdown-name']"
  logout_xpath="//a[normalize-space()='Logout']"

  click_admin_xpath = "//li[1]//a[1]//span[1]"
  click_add_user_xpath ="//button[contains(.,'Add')]"
  user_role_xpath = "(//div[@role='listbox']//child::div)[2]"
  status_xpath = "(//div[@role='listbox']//child::div)[1]"
  password_xpath = "//input[@class='oxd-input oxd-input--focus']"
  confirm_password_xpath = "//input[@class='oxd-input oxd-input--focus']"
  employee_name_xpath = "//input[@placeholder='Type for hints...']"
  username_xpath = "//input[@class='oxd-input oxd-input--focus oxd-input--error']"
  save_user_xpath = "//button[@type='submit']"
  cancel_user_xpath = "//button[normalize-space()='Cancel']"

  def __init__(self,driver):
      self.driver=driver
      self.wait = WebDriverWait(self.driver, 30)

  def Enter_username(self,username):
      self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,self.text_username_xpath)))
      self.driver.find_element(By.XPATH,self.text_username_xpath).send_keys(username)

  def Enter_password(self,password):
      self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,self.text_password_xpath)))
      self.driver.find_element(By.XPATH,self.text_password_xpath).send_keys(password)

  def Login_button_click(self):
      self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,self.login_button_xpath)))
      self.driver.find_element(By.XPATH,self.login_button_xpath).click()
  def menu_button_click(self):
      self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,self.menu_button_xpath)))
      self.driver.find_element(By.XPATH,self.menu_button_xpath).click()

  def logout_button_click(self):

      self.driver.find_element(By.XPATH,self.logout_xpath).click()

  def click_admin(self):
      self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,self.click_admin_xpath)))
      self.driver.find_element(By.XPATH,self.click_admin_xpath).click()

  def click_add_user(self):
      self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.click_add_user_xpath)))
      self.driver.find_element(By.XPATH,self.click_add_user_xpath).click()
  def select_user_role(self):
      drop_down=self.driver.find_element(By.XPATH,self.click_add_user_xpath)
      select_dropdown=Select(drop_down)
      self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,self.user_role_xpath)))
      select_dropdown.select_by_visible_text("Enabled")

  def enter_employee_name(self,employee_name):
      self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.employee_name_xpath)))
      self.driver.find_element(By.XPATH,self.employee_name_xpath).send_keys(employee_name)

  def select_status(self):
      self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.status_xpath)))
      select_status=self.driver.find_element(By.XPATH,self.status_xpath)
      time.sleep(5)
      select_status.select_by_index(1)
  def enter_username(self,new_username):
      self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.username_xpath)))
      self.driver.find_element(By.XPATH,self.username_xpath).send_keys(new_username)
  def enter_password(self,new_password):
      self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.password_xpath)))
      self.driver.find_element(By.XPATH,self.password_xpath).send_keys(new_password)
  def confirm_Password(self,confirm_password):
      self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.confirm_password_xpath)))
      self.driver.find_element(By.XPATH,self.confirm_password_xpath).send_keys(confirm_password)

  def click_save(self):
      self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.save_user_xpath)))
      self.driver.find_element(By.XPATH,self.save_user_xpath).click()



  def verify_login(self):
      try:
          self.driver.find_element(By.XPATH,self.menu_button_xpath)
          return "Login Successful"
      except:
          return "Login Unsuccessful"



