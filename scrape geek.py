# Import Module
import collections

from bs4 import BeautifulSoup
import requests
collections.Callable = collections.abc.Callable

if __name__ == '__main__':
    # Website URL
    URL = 'https://www.geeksforgeeks.org/'

    # class list set
    class_list = set()

    # Page content from Website URL
    page = requests.get( URL )

    # parse html content
    soup = BeautifulSoup( page.content , 'html.parser')
    for string in soup.stripped_strings:
        print(string)

