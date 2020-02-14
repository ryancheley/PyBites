import json
from collections import namedtuple
from typing import List

import requests
from bs4 import BeautifulSoup as Soup
from dateutil.parser import parse

PYCON_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/pycons.html"

PyCon = namedtuple("PyCon", "name city country start_date end_date url")

country_lookup = {
    "Africa": [
        "Algeria", "Angola", "Benin", "Botswana",
        "Burkina Faso", "Burundi", "Cameroon", "Cape Verde",
        "Central African Republic", "Chad", "Comoros",
        "Democratic Republic of the Congo",
        "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea",
        "Ethiopia", "Gabon", "Ghana", "Guinea", "Guinea-Bissau",
        "Ivory Coast", "Kenya", "Lesotho", "Liberia",
        "Libya", "Madagascar", "Malawi", "Mali",
        "Mauritania", "Mauritius", "Morocco", "Mozambique",
        "Namibia", "Niger", "Nigeria", "Republic of the Congo",
        "Rwanda", "São Tome and Principe", "Senegal", "Seychelles",
        "Sierra Leone", "Somalia", "South Africa", "South Sudan",
        "Sudan", "Swaziland", "Tanzania", "The Gambia",
        "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe",
    ],
    "Asia": [
        "Afghanistan", "Armenia", "Azerbaijan", "Bahrain",
        "Bangladesh", "Bhutan", "Brunei", "Cambodia",
        "China", "East Timor", "Georgia", "India",
        "Indonesia", "Iran", "Iraq", "Israel",
        "Japan", "Jordan", "Kazakhstan", "Kuwait",
        "Kyrgyzstan", "Laos", "Lebanon", "Malaysia",
        "Maldives", "Mongolia", "Myanmar", "Nepal",
        "North Korea", "Oman", "Pakistan", "Palestinian territories",
        "Philippines", "Qatar", "Saudi Arabia", "Singapore",
        "South Korea", "Sri Lanka", "Syria", "Taiwan",
        "Tajikistan", "Thailand", "Turkey", "Turkmenistan",
        "United Arab Emirates", "Uzbekistan", "Vietnam",
        "Yemen",
    ],
    "Australia and Oceania": [
        "Australia", "Federated States of Micronesia", "Fiji",
        "Kiribati", "Marshall Islands", "Nauru", "New Zealand",
        "Palau", "Papua New Guinea", "Samoa", "Solomon Islands",
        "Tonga", "Tuvalu", "Vanuatu",
    ],
    "Europe": [
        "Albania", "Andorra", "Austria", "Belarus", "Belgium",
        "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus",
        "Czech Republic", "Denmark", "Estonia", "Finland",
        "France", "Germany", "Greece", "Hungary", "Iceland",
        "Italy", "Latvia", "Liechtenstein", "Lithuania",
        "Luxembourg", "Malta", "Moldova", "Monaco",
        "Montenegro", "Netherlands", "Norway", "Poland",
        "Portugal", "Republic of Ireland", "Republic of Macedonia",
        "Romania", "Russia", "San Marino", "Serbia", "Slovakia",
        "Slovenia", "Spain", "Sweden", "Switzerland",
        "Ukraine", "United Kingdom", "U.K.", "Vatican City",
    ],
    "North America": [
        "Antigua and Barbuda", "Barbados", "Belize",
        "Canada", "Costa Rica", "Cuba", "Dominica",
        "Dominican Republic", "El Salvador", "Grenada",
        "Guatemala", "Haiti", "Honduras", "Jamaica",
        "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis",
        "Saint Lucia", "Saint Vincent and the Grenadines",
        "The Bahamas", "Trinidad and Tobago",
        "United States of America", "U.S.A.",
    ],
    "South America": [
        "Argentina", "Bolivia", "Brazil", "Chile",
        "Colombia", "Ecuador", "Guyana", "Paraguay",
        "Peru", "Suriname", "Uruguay", "Venezuela",
    ],
}


def get_continent(country: str) -> str:
    """
    Given a country name returns the associated continent of the country.

    :param country: The name of the country
    :type country: str
    :returns: The continent of the country
    :rtype: str
    """
    for continent, countries in country_lookup.items():
        for c in countries:
            if country.lower() in c.lower():
                return continent


def _get_pycon_data():
    """Helper function that retrieves the required PyCon data"""
    with requests.Session() as session:
        return session.get(PYCON_DATA).content.decode("utf-8")


def get_pycon_events(data=_get_pycon_data()) -> List[PyCon]:
    """
    Scrape the PyCon events from the given website data and
    return a list of PyCon namedtuples. Pay attention to the
    application/ld+json data structure website data.
    """
    soup = Soup(data, 'html.parser')
    script_list = []
    for s in soup.find_all('script', {'type': 'application/ld+json'}):
        parsed_data = json.loads("".join(s))
        p = PyCon(
            parsed_data['name'],
            parsed_data['location']['address']['addressLocality'],
            parsed_data['location']['address']['addressCountry'],
            parse(parsed_data['startDate']),
            parse(parsed_data['endDate']),
            parsed_data['url'],
        )
        script_list.append(p)

    return script_list


def filter_pycons(pycons: List[PyCon],
                  year: int = 2019,
                  continent: str = "Europe") -> List[PyCon]:
    """
    Given a list of PyCons a year and a continent return
    a list of PyCons that take place in that year and on
    that continent.
    """
    result = []
    for p in pycons:
        if p.start_date.year == year and get_continent(p.country) == continent:
            result.append(p)

    return result

f = filter_pycons(get_pycon_events(), 2019, 'Europe')
print(f)
# pytest Bite256/Bite256.py -vv
#
# import datetime
# import pytest
#
# @pytest.fixture(scope="session")
# def pycon_events():
#     events = get_pycon_events()
#     return events
#
# print(pycon_events)
#
# @pytest.fixture(scope="session")
# def filtered_pycons(pycon_events):
#     filtered = filter_pycons(pycon_events)
#     return filtered
#
#
# def test_get_pycon_events_number(pycon_events):
#     assert len(pycon_events) == 21
#
#
# def test_get_pycon_events_cities(pycon_events):
#     actual = {event.city for event in pycon_events}
#     expected = {
#         "Accra", "Belgrade", "Belgrade", "Berlin",
#         "Bratislava", "Cardiff", "Cleveland, OH", "Dublin",
#         "Florence", "Hyderabad", "Jakarta", "Johannesburg",
#         "Makati", "Munich", "Nairobi", "Odessa",
#         "Ostrava", "Puerto Vallarta", "Sydney",
#         "Taipei", "Toronto",
#     }
#     assert actual == expected
#
#
# def test_get_pycon_events_dates(pycon_events):
#     assert all(
#         isinstance(event.start_date, datetime.datetime)
#         for event in pycon_events
#     )
#     assert all(isinstance(event.end_date, datetime.datetime)
#                for event in pycon_events)
#
#
# def test_filter_pycons_number(filtered_pycons):
#     actual = len(filtered_pycons)
#     expected = 9
#     assert actual == expected
#
#
# def test_filter_pycons_cities(filtered_pycons):
#     actual = {event.city for event in filtered_pycons}
#     expected = {
#         "Belgrade", "Berlin", "Bratislava", "Cardiff",
#         "Dublin", "Florence", "Munich", "Odessa",
#         "Ostrava",
#     }
#     assert actual == expected
#
#
# def test_filter_pycons_dates(filtered_pycons):
#     assert all(
#         isinstance(event.start_date, datetime.datetime)
#         for event in filtered_pycons
#     )
#     assert all(
#         isinstance(event.end_date, datetime.datetime)
#         for event in filtered_pycons
#     )
#
#
# def test_filter_pycons_year(filtered_pycons):
#     actual = {pycon.start_date.year for pycon in filtered_pycons}
#     expected = {2019}
#     assert actual == expected
#
#
# def test_filter_pycons_continent(filtered_pycons):
#     actual = {get_continent(pycon.country) for pycon in filtered_pycons}
#     expected = {"Europe"}
#     assert actual == expected