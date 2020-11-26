class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(
			f"The name of the restaurant is {self.restaurant_name} and it "
			f"serves {self.cuisine_type}-type cuisine."
		)

	def open_restaurant(self):
		print(f"{self.restaurant_name} is currently open for business.")


restaurant = Restaurant("Wendy's", "burgers")
restaurant.describe_restaurant()
restaurant.open_restaurant()