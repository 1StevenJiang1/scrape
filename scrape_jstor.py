from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager


import time

if __name__ == '__main__':
    # Set options for headless browsing (if desired)
    chrome_options = Options()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])

    # allow for automatic downloads
    dl_path = r'C:\Users\yichj\Desktop\jstor_downloads'
    chrome_options.add_experimental_option('prefs', {
        "download.default_directory": dl_path,  # Change default directory for downloads
        "download.prompt_for_download": False,  # To auto download the file
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
    })

    # chrome_options.add_argument('--headless')

    # Create a Chrome WebDriver with the specified options and executable path
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 600)

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
    # while True:
    #     time.sleep(1)

    # pass the duo login page
    duo_frame = wait.until(EC.visibility_of_element_located((By.ID, 'duo_iframe')))
    driver.switch_to.frame(duo_frame)  # Switching to iframe by ID
    duo_buttons = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//button[@class='positive auth-button']")))
    duo_buttons[0].click()
    driver.switch_to.default_content()

    # Now begin downloading the first three pages
    i = 0
    while i < 3:

        # identify all the download buttons
        download_buttons = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "/html[@class='no-js']/body/main[@id='content']/div[@class='main-content-without-margin']/div[@id='search-results-vue-mount']/div/div[@class='search-results-area']/div[3]/div[@class='search-results-layout']/div[@class='search-results-layout__content']/ol[@class='search-results-layout__content__list']/li/div/div/div[@class='text-results']/ol[@class='result-list']/li[@class='result-list__item'][1]/div[@class='result']/div[@class='result__action-buttons']/ul[@class='action-buttons action-buttons--grouped']/li[@class='action-buttons__button search-result-action-button--download']/div/div/mfe-download-pharos-button")))
        for button in download_buttons:
            button.click()
            # proceed to downloading in the new window opened
            new_window = driver.window_handles[-1]
            driver.switch_to.window(new_window)
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 's')
            time.sleep(5)
        i += 1



    time.sleep(120)
    exit(1)

    # Enter the login credentials

