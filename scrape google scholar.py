import collections
import ssl
import sys
import urllib

import requests
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
import html_functions


if __name__ == '__main__':
    context = ssl._create_unverified_context()

    with urllib.request.urlopen('https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=black+cultural+capital&oq=', context=context) as response:
        # Read the response content
        html_content = response.read()
    soup = BeautifulSoup(html_content, 'html.parser')

    # You can now work with the parsed HTML using BeautifulSoup
    # For example, you can extract data or find specific elements
    title = soup.title
    print("Title:", title.text)