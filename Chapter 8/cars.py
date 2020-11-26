def cars(manufacturer, model_name, **options):
	options["Manufacturer"] = manufacturer
	options["Model Name"] = model_name
	return options


my_car = cars("Toyota", "Camry", color="Black", engine="V6")
print(my_car)
