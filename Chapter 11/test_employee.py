import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):

	def setUp(self):
		self.jared = Employee("Jared", "Winter", 100000)

	def test_give_default_raise(self):
		self.jared.give_raise()
		self.assertEqual(self.jared.salary, 105000)

	def test_give_custom_raise(self):
		self.jared.give_raise(10000)
		self.assertEqual(self.jared.salary, 110000)


if __name__ == '__main__':
	unittest.main()
