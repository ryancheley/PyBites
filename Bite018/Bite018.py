import os
import urllib.request
import re
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


def get_harry_most_common_word():
    stop_list = []
    stop = open(stopwords_file, 'r')
    for s in stop:
        stop_list.append(s.split('\n')[0].lower())

    harry = []
    harry_words = open(harry_text, 'r')
    for line in harry_words:
        for word in line.split():
            harry.append("".join(c for c in word if c.isalnum()).lower())

    filtered_list = [x for x in harry if x not in stop_list]
    cnt = Counter()
    for w in filtered_list:
        if w:
            cnt[w] += 1
    return (cnt.most_common()[0])


top_word = get_harry_most_common_word()
print(type(top_word))
print(top_word[0])
print(top_word[1])
