from collections import defaultdict
import os
from urllib.request import urlretrieve


from bs4 import BeautifulSoup


# prep data
tmp = os.getenv("TMP", "/tmp")
page = 'us_holidays.html'
holidays_page = os.path.join(tmp, page)
urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, 'html.parser')
    table_list = []
    for lt in soup.find_all("table", {"class": "list-table"}):
        for row in lt.find_all("tr"):
            table_list.append(row)
    data = []
    for t in table_list:
        try:
            data.append(
                (
                    t.find("time").text[5:7],
                    t.find("a").text.strip()
                )
            )
        except AttributeError:
            pass
    for k, v in data:
        holidays[k].append(v)
    return holidays['01']

x = get_us_bank_holidays(content)
print(x)
