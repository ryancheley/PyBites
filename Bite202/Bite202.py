import csv
import os
from pathlib import Path
from urllib.request import urlretrieve
from collections import defaultdict
import re

data = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
tmp = Path(os.getenv("TMP", "/tmp"))
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve(data, stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    d = defaultdict(list)
    bite_list = []
    result = []
    with open(stats, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            bite_list.append(row)
    bite_list = bite_list[1:]
    for bite in bite_list:
        bite[0] = re.search(r'\d+', re.search(r'Bite \d+', bite[0]).group()).group()
        try:
            if bite[1] != 'None':
                d[bite[0]] = float(bite[1])
        except IndexError:
            pass
    sorted_stats = sorted(d.items(), key=lambda k_v: k_v[1], reverse=True)
    for s in sorted_stats:
        result.append(s[0])
    return result[0:N]


if __name__ == '__main__':
    res = get_most_complex_bites(N=205)
    print(res)