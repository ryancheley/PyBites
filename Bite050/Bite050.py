from collections import namedtuple
from datetime import date
import re

import feedparser

FEED = 'https://bites-data.s3.us-east-2.amazonaws.com/all.rss.xml'

Entry = namedtuple('Entry', 'date title link tags')


def _convert_struct_time_to_dt(stime):
    """Convert a time.struct_time as returned by feedparser into a
    datetime.date object, so:
    time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
    -> date(2016, 12, 28)
    """
    return date(year=stime.tm_year, month=stime.tm_mon, day=stime.tm_mday)


def get_feed_entries(feed=FEED):
    """Use feedparser to parse PyBites RSS feed.
       Return a list of Entry namedtuples (date = date, drop time part)
    """
    result = []
    rss = feedparser.parse(feed)
    for r in rss['entries']:
        pub_dt = r['published_parsed']
        tags = []
        for t in r['tags']:
            tags.append(t['term'].lower())
        result.append(Entry(_convert_struct_time_to_dt(pub_dt), r['title'], r['link'], tags))

    return result


def filter_entries_by_tag(search, entry):
    """Check if search matches any tags as stored in the Entry namedtuple
       (case insensitive, only whole, not partial string matches).
       Returns bool: True if match, False if not.
       Supported searches:
       1. If & in search do AND match,
          e.g. flask&api should match entries with both tags
       2. Elif | in search do an OR match,
          e.g. flask|django should match entries with either tag
       3. Else: match if search is in tags
    """
    search_list = re.split('\||\&', search.lower())
    if re.search('\&', search):
        return all(elem in entry.tags for elem in search_list)
    elif re.search('\|', search):
        return any(elem in entry.tags for elem in search_list)
    else:
        return search_list[0] in list(entry.tags)


def main():
    """Entry point to the program
       1. Call get_feed_entries and store them in entries
       2. Initiate an infinite loop
       3. Ask user for a search term:
          - if enter was hit (empty string), print 'Please provide a search term'
          - if 'q' was entered, print 'Bye' and exit/break the infinite loop
       4. Filter/match the entries (see filter_entries_by_tag docstring)
       5. Print the title of each match ordered by date ascending
       6. Secondly, print the number of matches: 'n entries matched'
          (use entry if only 1 match)
    """
    entries = get_feed_entries()
    while True:
        term = input('Enter a Search term: ')
        if term == '':
            print('Please provide a search term')
        elif term == 'q':
            print('Bye')
            break
        else:
            return_list = []
            for e in entries:
                if filter_entries_by_tag(term, e):
                    # print(filter_entries_by_tag(term, e))
                    return_list.append((e.title, e.date))
            return_list = sorted(return_list, key = lambda x: x[1])
            if len(return_list) == 0:
                print('0 entries matched')
            else:
                for r in return_list:
                    print(r[0])
                if len(return_list) == 1:
                    print(f'{len(return_list)} entry matched')
                else:
                    print(f'{len(return_list)} entries matched')



if __name__ == '__main__':
    main()

