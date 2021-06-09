#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""

from collections import Counter
import operator

CHEESES = [
    "Red Leicester",
    "Tilsit",
    "Caerphilly",
    "Bel Paese",
    "Red Windsor",
    "Stilton",
    "Emmental",
    "Gruyère",
    "Norwegian Jarlsberg",
    "Liptauer",
    "Lancashire",
    "White Stilton",
    "Danish Blue",
    "Double Gloucester",
    "Cheshire",
    "Dorset Blue Vinney",
    "Brie",
    "Roquefort",
    "Pont l'Evêque",
    "Port Salut",
    "Savoyard",
    "Saint-Paulin",
    "Carré de l'Est",
    "Bresse-Bleu",
    "Boursin",
    "Camembert",
    "Gouda",
    "Edam",
    "Caithness",
    "Smoked Austrian",
    "Japanese Sage Derby",
    "Wensleydale",
    "Greek Feta",
    "Gorgonzola",
    "Parmesan",
    "Mozzarella",
    "Pipo Crème",
    "Danish Fynbo",
    "Czech sheep's milk",
    "Venezuelan Beaver Cheese",
    "Cheddar",
    "Ilchester",
    "Limburger",
]

RED_WINES = [
    "Châteauneuf-du-Pape",  # 95% of production is red
    "Syrah",
    "Merlot",
    "Cabernet sauvignon",
    "Malbec",
    "Pinot noir",
    "Zinfandel",
    "Sangiovese",
    "Barbera",
    "Barolo",
    "Rioja",
    "Garnacha",
]

WHITE_WINES = [
    "Chardonnay",
    "Sauvignon blanc",
    "Semillon",
    "Moscato",
    "Pinot grigio",
    "Gewürztraminer",
    "Riesling",
]

SPARKLING_WINES = [
    "Cava",
    "Champagne",
    "Crémant d’Alsace",
    "Moscato d’Asti",
    "Prosecco",
    "Franciacorta",
    "Lambrusco",
]


def _similar_name(cheese, wine):
    numberator = sum((Counter(cheese.lower()) & Counter(wine.lower())).values())
    denominator = (1 + pow(len(cheese) - len(wine), 2))
    return numberator / denominator


def best_match_per_wine(wine_type="all"):
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """
    if wine_type == 'red':
        wine_list = RED_WINES
    elif wine_type == 'white':
        wine_list = WHITE_WINES
    elif wine_type == 'sparkling':
        wine_list = SPARKLING_WINES
    elif wine_type == 'all':
        wine_list = RED_WINES + WHITE_WINES + SPARKLING_WINES
    else:
        raise ValueError

    results = []

    for cheese in CHEESES:
        for wine in wine_list:
            score_tuple = (wine, cheese, _similar_name(cheese, wine))
            results.append(score_tuple)

    results = sorted(results, key=lambda x: x[2], reverse=True)

    return results[0]


def match_wine_5cheeses():
    """  pairs all types of wines with cheeses ; returns a sorted list of tuples,
    where each tuple contains: wine, list of 5 best matching cheeses.
    List of cheeses is sorted by score descending then alphabetically ascending.
    e.g: [
    ('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer']),
    ...
    ...
    ('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
    ]
    """
    results = []
    cheeses = CHEESES
    wines = RED_WINES + WHITE_WINES + SPARKLING_WINES
    wines = sorted(wines)
    for wine in wines:
        cheese_score = []
        for cheese in cheeses:
            score_tuple = (wine, cheese, _similar_name(cheese, wine))
            cheese_score.append(score_tuple)
            cheese_score = sorted(cheese_score, key=lambda x: (-x[2], x[1]))[:5]
            cheese_value = [i[1] for i in cheese_score]
        results.append((wine, cheese_value))
    return results

    # return results


test = match_wine_5cheeses()
print(test)