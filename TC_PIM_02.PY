from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chrome WebDriver
driver = webdriver.Chrome()

# Open the OrangeHRM demo site
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Maximize the browser window
driver.maximize_window()

# Enter username
username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
username_field.send_keys("Admin")

# Enter password
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
password_field.send_keys("admin123")

# Login button and click it
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()

# PIM button and click it
Pim_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='PIM']")))
Pim_Button.click()

# Edit button and scroll into view
Edit_employee = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//i[@class='oxd-icon bi-pencil-fill']")))
driver.execute_script("arguments[0].scrollIntoView(true);", Edit_employee)

# JavaScript to click the edit button
driver.execute_script("arguments[0].click();", Edit_employee)

time.sleep(5)

# Updating the first name
First_name = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "firstName")))
First_name.clear()
First_name.send_keys("Vishagan")

# Updating the last name
last_name = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "middleName")))
last_name.clear()
last_name.send_keys("Kumar")

# Updating the date of birth
Dob = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='yyyy-dd-mm']")))
Dob.clear()
Dob.send_keys("2024-05-07")

# Save the updated details
save = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")))
driver.execute_script("arguments[0].scrollIntoView(true);", save)
driver.execute_script("arguments[0].click();", save)

time.sleep(10)

# Scroll the page to bring the Blood Type dropdown into view
Blood_type_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']")))
driver.execute_script("arguments[0].scrollIntoView(true);", Blood_type_dropdown)

# Try to click the dropdown
try:
    Blood_type_dropdown.click()
except:
    time.sleep(1)  # Wait a bit and retry if the element is blocked
    driver.execute_script("arguments[0].click();", Blood_type_dropdown)

# Select A+ from the dropdown
A_plus_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='option']/span[text()='A+']")))
A_plus_option.click()

# Save the blood type
save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")))
save_button.click()

# Add a delay to visualize the changes
time.sleep(10)

# Quit the driver
driver.quit()
