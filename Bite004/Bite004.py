import os
import re
from collections import Counter
import urllib.request

# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


# start coding

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    top_n_categories = []
    match = re.findall(r'<category>.*?<\/category>', content)
    match = Counter(match)
    for m in match.most_common(n):
        top_n_categories.append((m[0].replace('<category>', '').replace('</category>', ''), m[1]))
    return top_n_categories


g = get_pybites_top_tags(5)
print(g)