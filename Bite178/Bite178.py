from collections import Counter, defaultdict
import os
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    d = defaultdict(int)
    commits_list = []
    date_set = set()
    with open(commits, 'r') as f:
        for line in f:
            commits_list.append(
                line.replace('insertions(+)', '').
                    replace('deletions(-)', '').
                    replace('\n', '').
                    replace('insertion(+)', '').
                    replace('deletion(-)', '')
            )

    for c in commits_list:
        the_year = parse(c.split('|')[0].replace('Date:   ', '')).year
        the_month = parse(c.split('|')[0].replace('Date:   ', '')).month
        if year == the_year or year is None:
            try:
                changes = int(c.split('|')[1].split(',')[1]) + int(c.split('|')[1].split(',')[2])
            except IndexError:
                changes = int(c.split('|')[1].split(',')[1])
            date_set.add(
                (
                    YEAR_MONTH.format(
                        y=the_year,
                        m=the_month,
                    ),
                    changes
                )
            )

    for k, v in date_set:
        d[k] += v
    return min(d.items(), key=lambda a: a[1])[0], max(d.items(), key=lambda a: a[1])[0]

d = get_min_max_amount_of_commits(commits, 2017)
print(d)

