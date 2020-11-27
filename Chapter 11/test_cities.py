import unittest

from city_functions import city_functions


class CityTestCase(unittest.TestCase):

	def test_city_country(self):
		city_test = city_functions("santiago", "chile")
		self.assertEqual(city_test, "Santiago, Chile")


if __name__ == "__main__":
	unittest.main()
