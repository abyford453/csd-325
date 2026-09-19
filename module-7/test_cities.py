"""
Title: test_cities.py
Author: Drew Byford
Date: September 19, 2026
Description:
    This program uses Python's unittest module to test the
    city_country function.
"""

import unittest

from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    """Test cases for city_country()."""

    def test_city_country(self):
        """Test a city and country value."""
        formatted_location = city_country("santiago", "chile")
        self.assertEqual(formatted_location, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()