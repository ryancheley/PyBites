from itertools import permutations, combinations

friends = 'Bob Dante Julian Martin'.split()


def friends_teams(friends: list, team_size: int = 2, order_does_matter: bool = False):
    if order_does_matter:
        result = list(permutations(friends, team_size))
    else:
        result = list(combinations(friends, team_size))

    return result

f = friends_teams(friends, order_does_matter=False)

print(f)