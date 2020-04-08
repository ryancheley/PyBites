import operator
from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup

url = ("https://bites-data.s3.us-east-2.amazonaws.com/"
       "best-programming-books.html")
tmp = Path("/tmp")
html_file = tmp / "books.html"

if not html_file.exists():
    urlretrieve(url, html_file)


class Book:
    """Book class should instatiate the following variables:

    title - as it appears on the page
    author - should be entered as lastname, firstname
    year - four digit integer year that the book was published
    rank - integer rank to be updated once the books have been sorted
    rating - float as indicated on the page
    """
    def __init__(self, title, author, year, rank, rating):
        self.title = title
        self.author = author
        self.year = year
        self.rank = rank
        self.rating = float(rating)
        self.titlecase = title.title()

    def __str__(self):
        the_rank = '['+str(self.rank).rjust(3, '0')+'] '
        the_year = ' ('+str(self.year)+')'
        the_rating = str(self.rating)
        the_author = self.author
        book_display = the_rank\
                       +self.title\
                       +the_year\
                       +'\n      '\
                       +the_author\
                       + ' ' \
                       + the_rating
        return book_display


def _get_soup(file):
    return BeautifulSoup(file.read_text(), "html.parser")


def display_books(books, limit=10, year=None):
    """Prints the specified books to the console

    :param books: list of all the books
    :param limit: integer that indicates how many books to return
    :param year: integer indicating the oldest year to include
    :return: None
    """
    result = ''
    for b in books[:limit*2]:
        try:
            if b.year >= year:
                result = result + (b.__str__())+'\n'
        except TypeError:
            result = result + (b.__str__())+'\n'

    result = '\n'.join(result.rstrip().split('\n')[:limit*2])
    print(result)


def load_data():
    """Loads the data from the html file

    Creates the soup object and processes it to extract the information
    required to create the Book class objects and returns a sorted list
    of Book objects.

    Books should be sorted by rating, year, title, and then by author's
    last name. After the books have been sorted, the rank of each book
    should be updated to indicate this new sorting order.The Book object
    with the highest rating should be first and go down from there.
    """
    data = _get_soup(html_file)
    book_list = []
    html_books = data.find_all('div', {'class': 'book accepted normal'})

    for h in html_books:
        try:
            if 'python' in h.find_all('h2', {'class': 'main'})[0].text.lower():
                if len(h.find_all('h3', {'class': 'authors'})[0].find_all('a')[0].text.split()) == 2:
                    first_name = h.find_all('h3', {'class': 'authors'})[0].find_all('a')[0].text.split()[0]
                    last_name = h.find_all('h3', {'class': 'authors'})[0].find_all('a')[0].text.split()[-1]
                else:
                    first_name = ' '.join(h.find_all('h3', {'class': 'authors'})[0].find_all('a')[0].text.split()[:2])
                    last_name = h.find_all('h3', {'class': 'authors'})[0].find_all('a')[0].text.split()[-1]
                book_list.append(
                    Book(
                        # title, author, year, rank, rating
                        h.find_all('h2', {'class': 'main'})[0].text,
                        last_name+', '+first_name,
                        int(h.find_all('span', {'class': 'date'})[0].text.split()[1]),
                        int(h.find_all('div', {'class': 'rank'})[0].text),
                        float(h.find_all('span', {'class': 'our-rating'})[0].text)
                    )
                )
        except IndexError:
            pass
    # book_list_sort_by_year_title_author = sorted(book_list, key=operator.attrgetter('year', 'title', 'author'))
    book_list = sorted(book_list, key=operator.attrgetter('author'))
    book_list = sorted(book_list, key=operator.attrgetter('titlecase'))
    book_list = sorted(book_list, key=operator.attrgetter('year'))
    book_list = sorted(book_list, key=operator.attrgetter('rating'), reverse=True)
    for i, x in enumerate(book_list):
        x.rank = i+1
    return book_list


def main():
    books = load_data()
    display_books(books, limit=5, year=2017)
    """If done correctly, the previous function call should display the
    output below.
    """


if __name__ == "__main__":
    main()

"""
[001] Python Tricks (2017)
      Bader, Dan 4.74
[002] Mastering Deep Learning Fundamentals with Python (2019)
      Wilson, Richard 4.7
[006] Python Programming (2019)
      Fedden, Antony Mc 4.68
[007] Python Programming (2019)
      Mining, Joseph 4.68
[009] A Smarter Way to Learn Python (2017)
      Myers, Mark 4.66
"""