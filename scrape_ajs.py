from bs4 import BeautifulSoup
import time
import collections
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests

collections.Callable = collections.abc.Callable


if __name__ == '__main__':
    # Create a session object
    session = requests.Session()

    # Set the login credentials
    login_data = {
        'username': 'jiang664',
        'password': 'Qwe731970830'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.jstor.org',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

    # Perform the login request
    time.sleep(1)
    login_response = session.post('https://www.jstor.org/action/doBasicSearch?Query=sociology', headers=headers, data=login_data)

    # Check if the login is successful
    if login_response.status_code == 200:
        print("Login successful")

        # Continue accessing JSTOR using the session
        time.sleep(2)
        response = session.get('https://jstor.org')
        soup = BeautifulSoup(response.text, 'html.parser')
        print(response.text)  # JSTOR's HTML content

        with open('AJS_Result.txt', 'w', encoding='utf-8') as f:
            f.write(soup.prettify())
    else:
        print(login_response.status_code)
        print("Login failed")
