from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':
    # Set options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    # Path to the ChromeDriver executable
    chrome_driver_path = '/path/to/chromedriver'

    # Create a Chrome WebDriver with the specified options and executable path
    driver = webdriver.Chrome(options=chrome_options)

    # Set the login credentials
    username = 'jiang664'
    password = 'Qwe731970830'

    # Perform the login
    driver.get('https://www.jstor.org/action/doBasicSearch?Query=sociology')
    time.sleep(2)  # Wait for the page to load
    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.NAME, 'submit').click()

    # Wait for the login to complete and fetch the page source
    time.sleep(5)  # Adjust the delay as needed
    page_source = driver.page_source

    # Process the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    print(soup.prettify())

    # Close the browser
    driver.quit()
