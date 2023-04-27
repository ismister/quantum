import bs4
from googlesearch import search
import re
import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from urllib.parse import urlencode, urlparse, parse_qs
from lxml.html import fromstring
from requests import get


def get_wiki_txt(link):
    page = requests.get(link)

    soup = BeautifulSoup(page.content, 'html.parser')

    list(soup.children)
    return(soup.find_all('p')[0].get_text())


'''headers = {
    "Accept": '*/*',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'
}'''


def get_url(query):
        for j in search(query, tld="co.in", num=10, stop=10, pause=2):
            if re.match(r'https://ru.wikipedia.org', j) != None and j != "https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F":
                return "Посмотрите на этом сайте:\n" + j + "\n" + get_wiki_txt(j)
            return 'На данный запрос у меня нет ответа('



'''def get_source(url):
    """Return the source code for the provided URL.

    Args:
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html.
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)
def get_results(query):
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.com/search?q=" + query)
    return response
def parse_results(response):
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = "wDYxhc"

    results = response.html.find(css_identifier_result)

    output = []

    for result in results:
        item = {
            'link': result.find(css_identifier_link, first=True).attrs['href']
        }

        output.append(item)
    return output
def google_search(query):
    response = get_results(query)
    return parse_results(response)'''
