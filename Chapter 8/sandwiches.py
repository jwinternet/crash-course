def sandwich():
	order_list = []
	while True:
		order = input("\n What would you like on your sandwich? ")
		order_list.append(order)
		choice = input(
				" Would you like anything else on your sandwich? Enter 'y' "
				"for yes, and 'n' for no. "
		)
		if choice == "y":
			continue
		else:
			print("\n Your sandwich contains the following: ")
			for o in order_list:
				print(" - " + o)


sandwich()
