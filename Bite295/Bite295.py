from typing import List, Union
from functools import reduce


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if len(lst_of_lst) == 0:
        return None

    return reduce(lambda a, b:a+[sep]+b, lst_of_lst)