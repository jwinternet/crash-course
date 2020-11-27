with open("dogs_file.txt") as file:
	for f in file:
		x = f.replace("Python", "C++")
		print(x)
