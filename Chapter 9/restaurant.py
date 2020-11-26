class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 19108141

	def describe_restaurant(self):
		print(
			f"\nThe name of the restaurant is {self.restaurant_name} and it "
			f"serves {self.cuisine_type}-type cuisine."
		)

	def open_restaurant(self):
		print(f"{self.restaurant_name} is currently open for business.")

	def served(self):
		print(f"The restaurant has served {self.number_served} people.")

	def increment_served(self, more_served):
		self.number_served += more_served

	def reset_served(self):
		self.number_served = 0


class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ["vanilla", "chocolate", "strawberry"]

	def get_flavors(self):
		print(f"\nThe restaurant offers these flavors of ice cream:")
		for f in self.flavors:
			print(" - " + f)


restaurant = IceCreamStand("Wendy's", "burgers")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.served()

restaurant.get_flavors()
