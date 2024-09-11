from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

#orange HRM portal
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(3)

# enter a username
username_field = driver.find_element(By. NAME, "username")
username_field.send_keys("Admin")

time.sleep(2)

# enter a password
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("admin123")

time.sleep(2)

login_button = driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
login_button.click()


time.sleep(10)

print("logined succefully")

driver.quit()
