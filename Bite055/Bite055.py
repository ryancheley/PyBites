from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    game = []
    f = feedparser.parse(FEED_URL)
    data = f.get('entries')
    for i in data:
        game.append(Game(i.get('title'), i.get('link')))
    return game


games = get_games()
print(len(games))