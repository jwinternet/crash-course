from user_profile import UserProfile


class Admin(UserProfile):
	def __init__(self, first_name, last_name, username, country, posts):
		super().__init__(first_name, last_name, username, country, posts)
		self.privileges = Privileges([])


class Privileges:
	def __init__(self, privileges):
		self.privilege = privileges

	def show_privileges(self):
		print(f"\nThe user has the following privileges:")
		for p in self.privileges:
			print(" - " + p)
