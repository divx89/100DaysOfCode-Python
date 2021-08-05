# -*- coding: utf-8 -*-
"""
Dictionaries nested within list.
Adding a new dictionary to a list of dictionaries

Created on Thu Aug  5 13:17:18 2021

@author: divxd
"""

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country, visit_count, cities_visited):
    countryDict = {
        "country": country,
        "visits": visit_count,
        "cities": cities_visited
    }
    for index in range(len(travel_log)):
        if travel_log[index]["country"] == country:
            travel_log[index] = countryDict
            return
    travel_log.append(countryDict)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
