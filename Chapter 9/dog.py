class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sit(self):
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		print(f"{self.name} rolled over!")


my_dog = Dog("Jeffy", 10)
print(f"My dog's name is {my_dog.name} and they're {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()
