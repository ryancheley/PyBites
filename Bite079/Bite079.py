import csv
import requests
from collections import defaultdict

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    result = defaultdict(list)
    content_tuple = []
    internal_list = []
    with requests.Session() as s:
        download = s.get(CSV_URL)

        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')

        my_list = list(cr)
        for row in my_list:
            internal_list.append(row)

        for c in internal_list:
            content_tuple.append((c[2], c[1]))

        for k, v in content_tuple:
            if k != 'tz':
                result[k].append(v)

    return result


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
       and their corresponding member counts in pluses to standard output
    """
    result = content
    for k in sorted(result.keys()):
        print(k.ljust(21, ' '), '|', len(result[k])*'+')

d = create_user_bar_chart(get_csv())

