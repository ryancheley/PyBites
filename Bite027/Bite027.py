import json
import os
import re
from urllib.request import urlretrieve


TMP = os.getenv("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DATA = 'omdb_data'
MOVIES = os.path.join(TMP, DATA)
if not os.path.isfile(MOVIES):
    urlretrieve(os.path.join(S3, DATA), MOVIES)

def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    result = []
    with open(files, 'r') as file:
        for line in file:
            data = json.loads(line)
            result.append(data)
    return result




def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    result = []
    for m in movies:
        if 'Comedy' in m.get('Genre'):
            result.append(m.get('Title'))

    return result[0]



def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    result = []
    for m in movies:
        wins_text = re.search(r'\d+ wins', m.get('Awards'))
        wins = re.search(r'\d+', wins_text.group())
        result.append((m.get('Title'), int(wins.group())))
    sorted_result = sorted(result, key=lambda x: x[1], reverse=True)

    return sorted_result[0][0]



def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    result = []
    for m in movies:
        runtime = re.search(r'\d+', m.get('Runtime'))
        result.append((m.get('Title'), int(runtime.group())))
    sorted_result = sorted(result, key=lambda x: x[1], reverse=True)

    return sorted_result[0][0]

g = get_movie_longest_runtime(get_movie_data(MOVIES))
print(g)
