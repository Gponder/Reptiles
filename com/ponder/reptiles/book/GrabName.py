import requests
from bs4 import BeautifulSoup


def grab_name(url):
    book_tag = []
    resp = requests.get(url)
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    books = soup.select('div[class="xname"]')
    print(books)
    i = 0
    for book in books:
        if i < 1:
            i = i+1
            continue
        else:
            book_tag.append(book.find('a'))
    return book_tag

