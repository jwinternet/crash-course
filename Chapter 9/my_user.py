from user_profile import Admin

user = Admin("Jeff", "Skilling", "AskWhyAsshole1999", "USA", 2184)
user.describe_user()

user_privileges = {
	"can't reset passwords",
	"can moderate discussions",
	"can suspend accounts"
}
user.privileges.privileges = user_privileges
user.privileges.show_privileges()
