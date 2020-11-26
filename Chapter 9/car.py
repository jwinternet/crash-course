class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.make} {self.model} {self.year}"
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		self.odometer_reading = mileage


my_new_car = Car("Toyota", "Camry", 2012)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(102123)
my_new_car.read_odometer()
