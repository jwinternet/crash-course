class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 19108141

	def describe_restaurant(self):
		print(
			f"The name of the restaurant is {self.restaurant_name} and it "
			f"serves {self.cuisine_type}-type cuisine."
		)

	def open_restaurant(self):
		print(f"{self.restaurant_name} is currently open for business.")

	def served(self):
		print(f"The restaurant has served {self.number_served} people.")

	def increment_served(self, more_served):
		self.number_served += more_served


restaurant = Restaurant("Wendy's", "burgers")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.served()
restaurant.increment_served(56465)
restaurant.served()
