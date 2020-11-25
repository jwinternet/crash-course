def make_album(artist_name, album_title, number_of_songs=""):
	created_album = {
		"Artist Name": artist_name,
		"Album Title": album_title,
	}
	if number_of_songs:
		created_album.update({"Number of Songs": number_of_songs})
	return created_album


while True:
	name = input("\n Band Name: ")
	album = input(" Album Name: ")
	songs_amount_question = input(
			" Do you know how many songs are on the album? Enter 'y' for "
			"yes, 'n' for no.\n ")
	if songs_amount_question == 'y':
		songs = input(" Number of songs: ")
		new_album = make_album(name, album, songs)
		print(new_album)
	elif songs_amount_question == 'n':
		new_album = make_album(name, album)
		print(new_album)
