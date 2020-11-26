class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

	def get_descriptive_name(self):
		long_name = f"{self.make} {self.model} {self.year}"
		return long_name.title()


my_new_car = Car("Toyota", "Camry", 2012)
print(my_new_car.get_descriptive_name())