from typing import Dict, List
from keyword import iskeyword
from importlib import import_module
import builtins

scores = {
    "builtin": 1,
    "keyword": 2,
    "module": 3,
}


def score_objects(objects: List[str],
                  scores: Dict[str, int] = scores) -> int:
    score = 0
    for i in objects:
        if iskeyword(i):
            score += scores.get('keyword')
        if i == 'objects':
            score += scores.get('module')
        try:
            if import_module(i):
                score += scores.get('module')
        except ModuleNotFoundError:
            pass
        if i in dir(builtins):
            score += scores.get('builtin')

    return score
