def make_album(artist_name, album_title, number_of_songs=""):
	created_album = {
		"Artist Name": artist_name,
		"Album Title": album_title,
	}
	if number_of_songs:
		created_album.update({"Number of Songs": number_of_songs})
	return created_album


new_album = make_album("Metallica", "Master of Puppets")
print(new_album)
new_album = make_album("Megadeth", "Rust In Peace", 12)
print(new_album)