

def get_profile(name, age, *args, **kwargs):
    if not isinstance(age, int):
        raise ValueError
    if len(args) > 5:
        raise ValueError
    result = dict()
    result['name'] = name
    result['age'] = age
    if args:
        result['sports'] = sorted(list(args))
    if kwargs:
        result['awards'] = kwargs
    return result



print(get_profile('tim', 36))
print(get_profile('tim', 36, 'tennis', 'basketball'))
print(get_profile('tim', 36, 'tennis', 'basketball', champ='helped out team in crisis'))
t = get_profile('tim', 36, 'tennis', 'basketball',
                       service='going the extra mile for our customers',
                       champ='helped out the team in crisis',
                       attitude='unbeatable positive + uplifting')

print(t)