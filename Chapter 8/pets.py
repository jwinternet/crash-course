def describe_pet(animal_type, pet_name="jarvis"):
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name="abner", animal_type="pig")
describe_pet(animal_type="rat")
