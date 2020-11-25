def show_messages(messages):
	for m in messages:
		print(m)


def send_messages(messages):
	new_messages = []
	for m in messages:
		new_messages.append(m)
	return new_messages


messages_list = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
show_messages(messages_list)

message_results = send_messages(messages_list)
print(message_results)
