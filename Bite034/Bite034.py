from collections import namedtuple
from datetime import datetime

Transaction = namedtuple('Transaction', 'giver points date')
# https://twitter.com/raymondh/status/953173419486359552
Transaction.__new__.__defaults__ = (datetime.now(),)


class User:
    def __init__(self, user):
        self.user = user
        self._transactions = []

    @property
    def name(self):
        return self.user

    @property
    def karma(self):
        return self.karma

    def __add__(self, other):
        self._transactions.append(other)