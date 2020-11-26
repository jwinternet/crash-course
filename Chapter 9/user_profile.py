class UserProfile:
	def __init__(
			self, first_name, last_name, join_year, country, number_of_posts):
		self.first_name = first_name
		self.last_name = last_name
		self.join_year = join_year
		self.country = country
		self.number_of_posts = number_of_posts

	def describe_user(self):
		print(
			f"\nThe user {self.first_name} {self.last_name} joined the "
			f"website in {self.join_year}, is from {self.country} and has "
			f"posted on our site {self.number_of_posts} times!"
		)

	def greet_user(self):
		print(
			f"\nGood morning {self.first_name} {self.last_name}, have a "
			f"great rest of your day!"
		)


class Privileges:
	def __init__(self):
		self.privileges = ["can add post", "can delete post", "can ban user"]

	def show_privileges(self):
		print(f"\nThe user has the following privileges:")
		for p in self.privileges:
			print(" - " + p)


class Admin(UserProfile):
	def __init__(
			self, first_name, last_name, join_year, country, number_of_posts):
		super().__init__(
			first_name, last_name, join_year, country, number_of_posts)
		self.privileges = Privileges


new_user = Admin("Jeff", "Skilling", 2001, "USA", 2184)
new_user.describe_user()
new_user.greet_user()
new_user.privileges.show_privileges()
