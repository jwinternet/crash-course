import unittest

from city_functions import city_functions


class CityTestCase(unittest.TestCase):

	def test_city_country(self):
		city_test = city_functions("santiago", "chile")
		self.assertEqual(city_test, "Santiago, Chile")

	def test_city_country_population(self):
		city_test = city_functions("santiago", "chile", "1000000")
		self.assertEqual(city_test, "Santiago, Chile - Population 1000000")


if __name__ == "__main__":
	unittest.main()
