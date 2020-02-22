from collections import namedtuple
from operator import attrgetter

from bs4 import BeautifulSoup
import requests

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple('Entry', 'title points comments')


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    result = []
    soup = _create_soup_obj(url)
    titles = soup.find_all('span', {'class': 'title'})
    controls = soup.find_all('span', {'class': 'controls'})
    for i in range(len(titles)):
        title = titles[i].text.replace('\n', '')
        points = int(controls[i].find('span', {'class': 'smaller'}).text.split()[0])
        comments = int(controls[i].find('span', {'class': 'smaller'}).text.split()[-2])
        entry = Entry(title, points, comments)
        result.append(entry)

    result = sorted(result, key=attrgetter('points', 'comments'), reverse=True)

    return result[:top]

g = get_top_titles('https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html', top=5)
print(g)