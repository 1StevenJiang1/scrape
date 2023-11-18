from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import time

if __name__ == '__main__':
    # Set options for headless browsing (if desired)
    chrome_options = Options()
    # chrome_options.add_argument('--headless')

    # Create a Chrome WebDriver with the specified options and executable path
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 60)

    # Navigate to the JSTOR website and perform the login
    driver.get('https://www-jstor-org.myaccess.library.utoronto.ca/action/doBasicSearch?Query=sociology')

    # Find and interact with the login form elements
    login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@class='container']/div[2]/p/strong/a[@class='loginButton']")))
    login_button.click()

    user_name_field = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@class='container']/div[@class='row']/div[@class='col-md-4']/div[@class='login-box']/form/div[@class='form-group'][1]/input[@id='username']")))
    user_name_field.send_keys('jiang664')
    pw = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@class='container']/div[@class='row']/div[@class='col-md-4']/div[@class='login-box']/form/div[@class='form-group'][2]/input[@id='password']")))
    pw.send_keys("Qwe731970830")
    uoft_login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@class='container']/div[@class='row']/div[@class='col-md-4']/div[@class='login-box']/form/button[@class='btn btn-primary btn-lg']")))
    uoft_login_button.click()

    duo_frame = wait.until(EC.visibility_of_element_located((By.ID, 'duo_iframe')))
    driver.switch_to.frame(duo_frame)  # Switching to iframe by ID
    duo_buttons = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//button[@class='positive auth-button']")))
    duo_buttons[0].click()
    driver.switch_to.default_content()
    while True:
        time.sleep(1)
    exit(1)

    # Enter the login credentials

