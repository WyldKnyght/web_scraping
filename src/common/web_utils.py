#\src\common\web_utils.py

import requests
from bs4 import BeautifulSoup

def send_get_request(url):
    return requests.get(url)

def parse_html(response):
    return BeautifulSoup(response.text, "html.parser")

def extract_text(soup):
    return soup.get_text()

def extract_links(soup):
    # Extract all the links from the website
    links = []
    for link in soup.find_all('a'):
        if href := link.get('href'):
            links.append(href)
    return links

def get_website_name(url):
    return url.split("//")[-1].split("/")[0]
