import traceback

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
from fake_useragent import UserAgent
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


if __name__ == '__main__':
    try:
        volume = 129
        # Set options for headless browsing (if desired)
        chrome_options = uc.ChromeOptions()
        ua = UserAgent()
        user_agent = ua.random

        chrome_options.add_argument(f'--user-agent={user_agent}')

        # allow for automatic downloads
        dl_path = 'C:\\Users\\yichj\\Desktop\\jstor_downloads'
        chrome_options.add_experimental_option('prefs', {
            "download.default_directory": dl_path,  # Change default directory for downloads
            "download.prompt_for_download": False,  # To auto download the file
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
        })

        # chrome_options.add_argument('--headless')

        # Create a Chrome WebDriver with the specified options and executable path
        driver = uc.Chrome(options=chrome_options)
        wait = WebDriverWait(driver, 600)

        # Navigate to the JSTOR website and perform the login
        driver.get('https://www.journals.uchicago.edu/loi/ajs')
        driver.maximize_window()
        select_years = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@class='js-accordion__trigger "
                                                                                 "loi-accordion__trigger']")))
        select_years[5].click()

        # select year 2023 - 2017
        select_years_copy = []
        for year in select_years:
            text = year.text
            if text.isdigit() and int(text) > 2016:
                select_years_copy.append(year)
        select_years = select_years_copy[:]
        # remove 2023 and 2019 for they are expanded already
        select_years_copy.pop(0)
        select_years_copy.pop(3)
        for year in select_years_copy:
            year.click()


        seconds = random.uniform(1, 2)
        time.sleep(seconds)
        select_volumes = wait.until(
            EC.visibility_of_all_elements_located((By.XPATH, "//*[contains(@class, 'issue__cover-date')]")))
        for item in select_volumes:
            print(item.text)
        time.sleep(200)

        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL).click(select_volumes[0]).key_up(Keys.CONTROL).perform()

        driver.switch_to.window(driver.window_handles[-1])

        pdf_buttons = wait.until((EC.presence_of_all_elements_located((By.XPATH, "//span[@class='issue-item__btn__label' "
                                                                                 "and text()='PDF']"))))
        seconds = random.uniform(1, 2)
        time.sleep(seconds)
        # now the webpage displays the collection of journals of an individual volume. Click on the pdf buttons for
        # each journal, download from the proceeding download page, come back, and continue with the next journal
        for pdf_button in pdf_buttons:
            actions.key_down(Keys.CONTROL).click(pdf_button).key_up(Keys.CONTROL).perform()
            driver.switch_to.window(driver.window_handles[-1])
            wait.until(EC.presence_of_element_located(
                (By.XPATH, "//*[@class='drawerMenu dark slider skip-drawer submenu-visible']")))

            download_button = wait.until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'dropdown-trigger') "
                                                          "and contains(@class, 'btn') and contains("
                                                          "@class, 'btn--light') and contains(@class, "
                                                          "'btn--cta_roundedColored')]")))
            download_button.click()
            seconds = random.uniform(1, 2)
            time.sleep(seconds)

            download_pdf_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'download "
                                                                                       "list-button') and "
                                                                                       "@data-download-files-key='pdf']")))
            download_pdf_button.click()
            time.sleep(5)
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])
        with open("download_log.txt", "w") as f:
            f.write(f"Volume {volume} is completed")
        volume -= 1
    except Exception as e:
        # Handle the exception
        print(f"An error occurred: {e}")
        print("Full traceback:")
        traceback.print_exc()

        # Optionally, you can capture the traceback as a string
        # if you want to log it to a file or process it further
        error_traceback = traceback.format_exc()
    input('press enter to continue')
