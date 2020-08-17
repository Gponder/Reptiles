import requests
from bs4 import BeautifulSoup

url = 'http://www.xuanshu.com/sort/1.html'


def grab_name():
    resp = requests.get(url)
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    books = soup.select('div[class="xname"]')
    i = 0
    for key in books:
        i = i+1
        if i < 2:
            continue
        else:
            print(key)


grab_name()
