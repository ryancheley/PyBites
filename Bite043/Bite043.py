# def get_profile(**kwargs):
#     name = kwargs.get('name', 'julian')
#     profession = kwargs.get('profession', 'programmer')
#     if kwargs.get('name') is None and kwargs.get('profession') is None and len(kwargs) > 0:
#         raise TypeError
#     elif (kwargs.get('name') is None or kwargs.get('profession') is None) and len(kwargs) > 1:
#         raise TypeError
#     elif kwargs.get('name') is not None and kwargs.get('profession') is not None and len(kwargs) > 2:
#         raise TypeError
#     else:
#         return f'{name} is a {profession}'


def get_profile(*, name='julian', profession='programmer'):
    return f'{name} is a {profession}'

t = get_profile(name='bob', profession='software developer')
print(t)