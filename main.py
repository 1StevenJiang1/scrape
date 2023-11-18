import requests
from bs4 import BeautifulSoup
import collections
collections.Callable = collections.abc.Callable

if __name__ == '__main__':
    source_code = """<span class="UserName"><a href="#">Martin Elias</a></span>"""
    soup = BeautifulSoup(source_code, 'html.parser')
    tag = soup.span.contents
    print(tag)

