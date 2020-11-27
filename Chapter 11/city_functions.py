def city_functions(city, country, population=""):
	if population:
		combined = city + ", " + country + " - population " + population
	else:
		combined = city + ", " + country
	return combined.title()
