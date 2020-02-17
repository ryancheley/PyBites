from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'html.parser')
    title = soup.find('div', {'class': 'dotd-title'}).text
    title = title.replace('\t', '').replace('\n', '')
    link = soup.find_all('div', {'class': 'dotd-main-book-image float-left'})[0].a.attrs['href']
    image = soup.find_all('div', {'class': 'dotd-main-book-image float-left'})[0].noscript.img.attrs['src']
    description = soup.find_all('div', {'class': 'dotd-main-book-summary float-left'})[0].contents[7].text
    description = description.replace('\t', '').replace('\n', '')

    book = Book(
        title,
        description,
        image,
        link
    )

    return book

g = get_book()

print(g)