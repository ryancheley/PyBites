from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name')

color_card_count = {
    '0': 1,
    '1': 2,
    '2': 2,
    '3': 2,
    '4': 2,
    '5': 2,
    '6': 2,
    '7': 2,
    '8': 2,
    '9': 2,
    'Skip': 2,
    'Reverse': 2,
    'Draw Two': 2,
}

non_color_card_count = {
    'Wild': 4,
    'Wild Draw Four': 4
}

def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    deck = []
    # add suited cards
    for color in SUITS:
        for i in color_card_count.items():
            for j in range(i[1]):
                deck.append(UnoCard(color, i[0]))

    # add non-suited cards
    for i in non_color_card_count.items():
        for j in range(i[1]):
            deck.append(UnoCard(None, i[0]))

    return deck
