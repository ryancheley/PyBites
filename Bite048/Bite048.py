import os
import urllib.request
import re
from collections import defaultdict

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)


def create_chart():
    logs = []
    result = []
    d = defaultdict(list)

    with open(SAFARI_LOGS, 'r') as f:
        for line in f:
            logs.append(line)

    for previous, current in zip(logs, logs[1:]):
        if re.search(r'sending to slack channel', current):
            if 'python' in previous.lower().split():
                result.append((previous.split()[0], PY_BOOK))
            else:
                result.append((previous.split()[0], OTHER_BOOK))
    for k, v in result:
        d[k].append(v)

    for k, v in d.items():
        print(k+' '+''.join(v))


c = create_chart()