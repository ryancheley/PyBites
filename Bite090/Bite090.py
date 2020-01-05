from collections import Counter, defaultdict
import csv

import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    season = content
    answer = defaultdict(list)
    result = []
    result_dict = {}
    data = [row for row in csv.reader(season.splitlines())]
    for d in data:
        try:
            result.append(
                (
                    d[2],
                    (
                        d[1],
                        len(d[3].split())
                    ),
                 )
            )
        except ValueError:
            pass
    for k, v in result:
        answer[k].append(v)
    for k in answer.keys():
        cnt = Counter()
        for e in answer[k]:
            cnt[e[0]] = cnt[e[0]]+e[1]
        result_dict.update({k: cnt})
    return result_dict
