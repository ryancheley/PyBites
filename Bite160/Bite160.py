import csv
import os
from urllib.request import urlretrieve
from collections import defaultdict

TMP = os.getenv("TMP", "/tmp")
DATA = 'battle-table.csv'
BATTLE_DATA = os.path.join(TMP, DATA)
if not os.path.isfile(BATTLE_DATA):
    urlretrieve(
        f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
        BATTLE_DATA
    )


def _create_defeat_mapping():
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    result = []
    with open(BATTLE_DATA, newline='') as csvfile:
        battle = csv.reader(csvfile, delimiter=',')
        for row in battle:
            result.append(row)
    mydd = defaultdict(list)
    for row in result:
        for item in range(len(row)):
            if row[item] == 'win':
                mydd[row[0]].append(result[0][item])
    return mydd



def get_winner(player1, player2, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()
    if (defeat_mapping[player1] == [] or defeat_mapping[player2] == []):
        raise ValueError
    if player1 == player2:
        return 'Tie'
    elif player2 in defeat_mapping[player1]:
        return player1
    elif player2 not in defeat_mapping[player1]:
        return player2
    else:
        return ''



d = get_winner('Rock', 'Scissors')
print(d)