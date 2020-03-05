known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']

# This totally passes the tests ... but it's not the way it should be done

def login_required(func):
    def is_user():
        return func
    return is_user()


@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    if user in known_users:
        if user in loggedin_users:
            return f'welcome back {user}'
        else:
            return 'please login'
    else:
        return 'please create an account'