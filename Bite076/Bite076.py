from functools import singledispatch
from datetime import datetime
import re
from itertools import compress

@singledispatch
def count_down(data_type):
    return data_type


@count_down.register(str)
@count_down.register(int)
@count_down.register(float)
def to_str(data_type):
    data_type_str = str(data_type)
    for t in range(len(data_type_str)):
        if t == 0:
            print(data_type_str)
        else:
            print(data_type_str[:-t])


@count_down.register(list)
def to_list(data_type):
    for t in range(len(data_type)):
        if t > 0:
            data_type.pop()
        print(*data_type, sep='')


@count_down.register(range)
@count_down.register(set)
@count_down.register(tuple)
@count_down.register(dict)
def to_list(data_type):
    data_type_list = list(data_type)
    for t in range(len(data_type_list)):
        if t > 0:
            data_type_list.pop()
        print(*data_type_list, sep='')


@count_down.register(re.Pattern)
@count_down.register(compress)
@count_down.register(datetime)
def catch_errors(data_type):
    raise ValueError