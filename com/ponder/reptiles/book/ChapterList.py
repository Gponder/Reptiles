import requests
from bs4 import BeautifulSoup


def get_chapter_list(url):
    result = []
    resp = requests.get(url)
    resp.encoding = resp.apparent_encoding
    soup = BeautifulSoup(resp.text, 'html.parser')
    list_div = soup.select_one('div[class="pc_list"]')
    chapter_list = list_div.find_all('a')
    for chapter in chapter_list:
        result.append(chapter)
    return result
