from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# Orange HRM portal
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# Enter username
username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
username_field.send_keys("Admin")

# Enter password
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
password_field.send_keys("admin123")

# Click login button
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()

# PIM button 
Pim_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='PIM']")))
Pim_Button.click()

# Locate the first checkbox
check_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[@class='oxd-icon bi-check oxd-checkbox-input-icon'])[1]")))

driver.execute_script("arguments[0].scrollIntoView(true);", check_box)

# Click the checkbox
driver.execute_script("arguments[0].click();", check_box)

# delete button and click it
delete_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-trash']")))
delete_button.click()

time.sleep(5)

# Confirm delete
click_yes = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']")))
click_yes.click()

time.sleep(5)

driver.quit()
