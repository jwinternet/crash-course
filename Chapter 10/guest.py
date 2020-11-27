user_name = input("Enter your name: ")

with open("new_file.txt", "w") as file:
	file.write(user_name)
