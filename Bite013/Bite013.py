from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here
BlogNT = namedtuple(
    'BlogNT',
    'name founders started tags location site'
)

def dict2nt(dict_):
    b1 = BlogNT(
        blog.get('name'),
        blog.get('founders'),
        blog.get('started'),
        blog.get('tags'),
        blog.get('location'),
        blog.get('site'),
    )
    return b1


def nt2json(nt):

    result = json.dumps(nt._asdict(), default=str)
    return result

n = nt2json(dict2nt(blog))
print(n)