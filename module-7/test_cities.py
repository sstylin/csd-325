
# Steve Stylin@Bellevue University
#Module 7.2 Test Cases
# test_cities.py

import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        """Test the city_country function with various inputs."""
        self.assertEqual(city_country("Santiago", "Chile"), "Santiago, Chile")
        self.assertEqual(city_country("Paris", "France"), "Paris, France")
        self.assertEqual(city_country("Montreal", "Canada"), "Montreal, Canada")

if __name__ == '__main__':
    unittest.main()
