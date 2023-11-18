import collections
import sys

import requests
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
import html_functions


if __name__ == '__main__':
    search_query = ''
    url = f'https://www.journals.uchicago.edu/doi/10.1086/219693{search_query}'
    try:
        response = requests.get(url)
    except:
        print('connection failed')
        sys.exit()
    soup = BeautifulSoup(response.content, 'html.parser')
    with open('scrape_result_raw.txt', 'w') as f:
        sib1 = soup.div
        print(type(sib1))
        content = soup.prettify()
        f.write(str(sib1))
    paper_results = soup.find_all('div', class_='gs_r gs_or gs_scl')
    for i in range(len(paper_results)):
        paper_results[i] = paper_results[i].prettify()
    with open('find_all.txt', 'w', encoding='utf-8') as f:
        for result in paper_results:
            f.write(f'{result}\n')
    paper_results = soup.stripped_strings
    with open('content_result.txt', 'w', encoding='utf-8') as f:
        for result in paper_results:
            f.write(f'{result}\n')
    a = 1
    # with open('scrape_result.txt', 'w', encoding='utf-8') as txtfile:
    #     for result in paper_results:
    #         title = result.find('h3', class_='gs_rt').text
    #         authors = result.find('div', class_='gs_a').text
    #         abstract = result.find('div', class_='gs_rs').text
    #
    #         # Write the scraped data into the text file
    #         txtfile.write(f'Title: {title}\n')
    #         txtfile.write(f'Authors: {authors}\n')
    #         txtfile.write(f'Abstract: {abstract}\n')
    #         txtfile.write('\n')


