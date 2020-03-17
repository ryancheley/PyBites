from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here


class UserDoesNotExist(Exception):
    pass


class UserAccessExpired(Exception):
    pass


class UserNoPermission(Exception):
    pass


def get_secret_token(username):
    if username not in [i.name for i in USERS]:
        raise UserDoesNotExist
    if username in [i.name for i in USERS if i.role == USER and i.expired == False]:
        raise UserNoPermission
    if username in [i.name for i in USERS if i.expired == True]:
        raise UserAccessExpired
    if username in [i.name for i in USERS if i.expired == False and i.role==ADMIN]:
        return SECRET



g = get_secret_token('PyBites')
print(g)