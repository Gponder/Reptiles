import requests
from bs4 import BeautifulSoup


def get_content(url):
    resp = requests.get(url)
    resp.encoding = resp.apparent_encoding
    soup = BeautifulSoup(resp.text, 'html.parser')
    content = soup.select_one('div[id="content1"]')
    return content.text


