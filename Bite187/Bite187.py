from dataclasses import dataclass
from math import floor

from dateutil.parser import *


@dataclass
class Actor:
    name: str
    born: str


@dataclass
class Movie:
    title: str
    release_date: str


def get_age(actor: Actor, movie: Movie) -> str:
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    date_of_birth = parse(actor.born)
    date_of_release = parse(movie.release_date)
    age = floor((date_of_release - date_of_birth).days / 365.25)
    name = actor.name
    title = movie.title
    result = f'{name} was {age} years old when {title} came out.'
    return result
