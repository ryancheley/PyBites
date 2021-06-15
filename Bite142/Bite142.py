from collections import namedtuple

MIN_SCORE = 4
DICE_VALUES = range(1, 7)

Player = namedtuple('Player', 'name scores')


def calculate_score(scores):
    """Based on a list of score ints (dice roll), calculate the
       total score only taking into account >= MIN_SCORE
       (= eyes of the dice roll).

       If one of the scores is not a valid dice roll (1-6)
       raise a ValueError.

       Returns int of the sum of the scores.
    """
    total_score = []
    for score in scores:
        if score not in DICE_VALUES:
            raise ValueError
        if score >= MIN_SCORE:
            total_score.append((score))
    return sum(total_score)


def get_winner(players):
    """Given a list of Player namedtuples return the player
       with the highest score using calculate_score.

       If the length of the scores lists of the players passed in
       don't match up raise a ValueError.

       Returns a Player namedtuple of the winner.
       You can assume there is only one winner.

       For example - input:
         Player(name='player 1', scores=[1, 3, 2, 5])
         Player(name='player 2', scores=[1, 1, 1, 1])
         Player(name='player 3', scores=[4, 5, 1, 2])

       output:
         Player(name='player 3', scores=[4, 5, 1, 2])
    """
    total_scores = []
    score_length = set()
    for player in players:
        score_length.add(len(player.scores))
        if len(score_length) > 1:
            raise ValueError
        total_scores.append(calculate_score(player.scores))

    return players[total_scores.index(max(total_scores))]

players = [
  Player(name='player 1', scores=[1, 3, 2, 5]),
  Player(name='player 2', scores=[1, 1, 1, 1]),
  Player(name='player 3', scores=[4, 5, 1, 2]),  # max 9
]

test = get_winner(players)
print(test)