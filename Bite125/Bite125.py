from collections import Counter

from bs4 import BeautifulSoup
import requests

AMAZON = "amazon.com"
# static copy
TIM_BLOG = ('https://bites-data.s3.us-east-2.amazonaws.com/'
            'tribe-mentors-books.html')
MIN_COUNT = 3


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode('utf-8')


def get_top_books(content=None):
    """Make a BeautifulSoup object loading in content,
       find all links that contain AMAZON, extract the book title
       and count them.
       Return a list of (title, count) tuples where
       count is at least MIN_COUNT
    """
    if content is None:
        content = load_page()
    amazon_books = []
    soup = BeautifulSoup(content, 'html.parser')
    for s in soup.find_all('a'):
        if 'amazon' in s.attrs['href'].lower():
            amazon_books.append(s.text)

    c = Counter(amazon_books)

    result = []
    for elem in c:
        if c[elem] >= MIN_COUNT:
            result.append((elem, c[elem]))

    return result

print(get_top_books())