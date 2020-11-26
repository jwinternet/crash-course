class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f"\n{self.make} {self.model} {self.year}"
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("\nYou can't roll back an odometer!")

	def increment_odometer(self, miles):
		self.odometer_reading += miles


my_new_car = Car("Toyota", "Camry", 2012)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(12210)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(21600)
my_used_car.read_odometer()
my_used_car.increment_odometer(7156)
my_used_car.read_odometer()
