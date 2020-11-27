from random import randint


class Die:
	def __init__(self):
		self.sides = 6

	def roll_die(self):
		for my_result in range(10):
			result = randint(1, self.sides)
			print(result)


my_roll = Die()
my_roll.roll_die()
