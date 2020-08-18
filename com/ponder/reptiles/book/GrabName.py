import requests
from bs4 import BeautifulSoup

url = 'http://www.xuanshu.com/sort/1.html'


def grab_name():
    book_tag = []
    resp = requests.get(url)
    html = resp.text
    print(html)
    soup = BeautifulSoup(html, 'html.parser')
    books = soup.select('div[class="xname"]')
    i = 0
    for book in books:
        if i < 1:
            continue
        else:
            book_tag.append(book.find('a'))
        i = i+1
    return book_tag


grab_name()
