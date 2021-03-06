MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __setitem__(self, name, birthday):
        if birthday.day in [i.day for i in list(self.values())] and birthday.month in [i.month for i in list(self.values())]:
            print(MSG.format(name))
        dict.__setitem__(self, name, birthday)

