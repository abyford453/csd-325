"""
Title: city_functions.py
Author: Drew Byford
Date: September 19, 2026
Description:
    This program formats information about a city. City and country
    are required, while population and language are optional.
"""


def city_country(city, country, population=None, language=None):
    """
    Return a formatted string containing city information.

    City and country are required.
    Population and language are optional.
    """
    location = f"{city.title()}, {country.title()}"

    if population is not None:
        location += f" - population {population}"

    if language is not None:
        location += f", {language.title()}"

    return location


if __name__ == "__main__":
    # City and Country.
    print(city_country("santiago", "chile"))

    # City, Country, and Population.
    print(city_country("london", "england", 9000000))

    # City, Country, Population, and Language.
    print(city_country("tokyo", "japan", 14000000, "japanese"))