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

# login button
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()

# PIM button 
Pim_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='PIM']")))
Pim_Button.click()

# Add Employee button 
add_employee = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")))
add_employee.click()

# Enter first name and last name
First_name = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "firstName")))
First_name.send_keys("Vishagan")

last_name = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "lastName")))
last_name.send_keys("Kumar")

# Enter employee ID
employee_id = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@class='oxd-input oxd-input--active']")))
employee_id.clear()
employee_id.send_keys("04022")

# save button to add employee
save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
save_button.click()

time.sleep(5)  

#  the Date of Birth field
Dob = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@fdprocessedid='zz37me']")))
Dob.send_keys("2024-05-07")

# Scroll and click the save button to save the updated details
save = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
driver.execute_script("arguments[0].scrollIntoView(true);", save)
save.click()

time.sleep(5)  

# Go back to PIM page
Pim_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='PIM']")))
Pim_Button.click()

# Quit the driver
driver.quit()
