import re
from typing import List

# https://stackoverflow.com/a/43147265
# just for exercise sake, real life use emoji lib
IS_EMOJI = re.compile(r'[^\w\s,]')


text = 'Books can be boring 😴, better to code 💪❗'

def get_emoji_indices(text: str) -> List[int]:
    """Given a text return indices of emoji characters"""
    answer = []
    result = [i for i in text]
    for r in range(len(result)):
        if IS_EMOJI.search(result[r]):
            answer.append(r)
    return answer




e = get_emoji_indices(text)
print(e)
