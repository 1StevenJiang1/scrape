import sys

import requests
from bs4 import BeautifulSoup


def get_attraibutes(soup: BeautifulSoup) -> set:
    class_list = set()
    # get all tags
    tags = {tag.name for tag in soup.find_all()}

    # iterate all tags
    for tag in tags:
        # find all element of tag
        for attrib in soup.find_all(tag):
            # if tag has attribute of class
            if attrib.has_attr("class"):
                if len(attrib['class']) != 0:
                    class_list.add(" ".join(attrib['class']))

    return class_list


def see_format(url: str, search_term, f_name: str) -> None:
    query = url + search_term
    try:
        response = requests.get(query)
        soup = BeautifulSoup(response.content, 'html.parser')
        with open(f_name, 'w', encoding='utf-8') as f:
            for item in soup.stripped_strings:
                f.write(item + '\n')
    except:
        print('connection failed')



