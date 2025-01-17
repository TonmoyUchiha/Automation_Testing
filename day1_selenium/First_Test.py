from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open URL
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # Wait for the username field and enter the username
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )
    username_field.send_keys("Admin")

    # Wait for the password field and enter the password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("admin123")

    # Wait for the login button and click it
    login_button = driver.find_element(By.CLASS_NAME, "orangehrm-login-button")
    login_button.click()

    # Wait for the dashboard page title
    WebDriverWait(driver, 10).until(EC.title_contains("OrangeHRM"))

    # Verify the page title
    act_title = driver.title
    exp_title = "OrangeHRM"
    if act_title == exp_title:
        print("Login Test Passed")
    else:
        print("Login Test Failed")
finally:
    # Close the browser
    driver.quit()
