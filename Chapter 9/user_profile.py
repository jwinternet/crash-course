class UserProfile:
	def __init__(
			self, first_name, last_name, username, country, posts):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.country = country
		self.posts = posts
		self.login_attempts = 0

	def describe_user(self):
		print(
			f"\nThe user {self.first_name} {self.last_name} joined the "
			f"website as {self.username}, is from {self.country} and has "
			f"posted on our site {self.posts} times!"
		)

	def greet_user(self):
		print(
			f"\nGood morning {self.first_name} {self.last_name}, have a "
			f"great rest of your day!"
		)

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0
