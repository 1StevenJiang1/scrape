from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from fake_useragent import UserAgent

import undetected_chromedriver as uc
import time

chrome_options = uc.ChromeOptions()
# chrome_options.add_experimental_option("useAutomationExtension", False)
# chrome_options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])

ua = UserAgent()
user_agent = ua.random

chrome_options.add_argument(f'--user-agent={user_agent}')

dl_path = 'C:\\Users\\yichj\\Desktop\\jstor_downloads'
chrome_options.add_experimental_option('prefs', {
    "download.default_directory": dl_path,  # Change default directory for downloads
    "download.prompt_for_download": False,  # To auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
})

# chrome_options.add_argument('--headless')

# Create a Chrome WebDriver with the specified options and executable path
# driver = webdriver.Chrome(options=chrome_options)

driver = uc.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 600)

# Navigate to the JSTOR website and perform the login
driver.get('https://www.journals.uchicago.edu/doi/epdf/10.1086/728613')


time.sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class='drawerMenu dark slider skip-drawer submenu-visible']")))

download_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'dropdown-trigger') "
                                                                       "and contains(@class, 'btn') and contains("
                                                                       "@class, 'btn--light') and contains(@class, "
                                                                       "'btn--cta_roundedColored')]")))
download_button.click()

download_pdf_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'download list-button') and @data-download-files-key='pdf']")))

download_pdf_button.click()

input('')