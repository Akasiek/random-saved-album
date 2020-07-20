import random
from time import sleep
import tekore as tk

# Authorization
conf = tk.config_from_file('conf.txt')
token = tk.prompt_for_user_token(
    *conf, scope=tk.scope.user_library_read + tk.scope.user_modify_playback_state)
spotify = tk.Spotify(token)

# Getting the number of all saved albums
albums_number = spotify.saved_albums(limit=1).total
albums = {}

if albums_number == 0:
    print("You don't have any saved albums")
    sleep(2)

else:
    # Appending all albums into the tabel
    # Sleep is for not getting a limit error
    for album in range(albums_number):
        albums[album] = spotify.saved_albums(
            limit=1, offset=album).items[0].album
        sleep(0.02)

    # Getting random number and selecting the album by this number
    random_number = random.randint(1, albums_number)
    selected_album = albums[random_number]

    # Playing the selected album
    print(
        f"Album has been selected. Now playing '{selected_album.name}' by {selected_album.artists[0].name} on Spotify")
    selected_album_uri = tk.to_uri('album', selected_album.id)
    spotify.playback_start_context(selected_album_uri)
