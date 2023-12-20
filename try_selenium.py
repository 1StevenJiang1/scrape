import json

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()
dl_path = r'C:\Users\yichj\Desktop\jstor_downloads'
options.add_experimental_option('prefs', {
"download.default_directory": dl_path, #Change default directory for downloads
"download.prompt_for_download": False, #To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})
driver = webdriver.Chrome(options=options)


driver.get('https://www.google.com/search?q=random+pdf&rlz=1C1CHBF_enCA974CA974&oq=random+pdf&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIPCAEQABhDGLEDGIAEGIoFMgwIAhAAGEMYgAQYigUyDwgDEAAYQxixAxiABBiKBTIMCAQQABhDGIAEGIoFMg8IBRAAGEMYsQMYgAQYigUyDAgGEAAYQxiABBiKBTIMCAcQABhDGIAEGIoFMgwICBAAGBQYhwIYgAQyCggJEAAYsQMYgATSAQgxNDk2ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8')
time.sleep(2)
button_1 = driver.find_element(By.XPATH, "/html/body[@id='gsr']/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[@id='center_col']/div[@id='res']/div[@id='search']/div/div[@id='rso']/div[@class='MjjYud'][1]/div[@class='g Ww4FFb vt6azd tF2Cxc asEBEc']/div[@class='N54PNb BToiNc cvP2Ce']/div[@class='kb0PBd cvP2Ce jGGQ5e']/div[@class='yuRUbf']/div/span/a/h3[@class='LC20lb MBeuO DKV0Md']")
button_1.click()
input('press enter')
button_2 = driver.find_element(By.XPATH, "/html/body[@id='gsr']/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[@id='center_col']/div[@id='res']/div[@id='search']/div/div[@id='rso']/div[@class='MjjYud'][2]/div[@class='g Ww4FFb vt6azd tF2Cxc asEBEc']/div[@class='N54PNb BToiNc cvP2Ce']/div[@class='kb0PBd cvP2Ce jGGQ5e']/div[@class='yuRUbf']/div/span/a/h3[@class='LC20lb MBeuO DKV0Md']")
button_2.click()

# Find the button using XPath
# button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/section[1]/div/div/div/form/button/span')

# Click on the button
# button.click()


time.sleep(500)

driver.quit()
