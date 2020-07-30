import random
from time import sleep
import tekore as tk
from colorTerminal import ColorTerminal as ct


def choosingRandomAlbum(albums_number):
    # Selecting random number and then album
    random_number = random.randint(0, albums_number-1)
    selected_album = spotify.saved_albums(
        limit=1, offset=random_number).items[0].album

    # Loop for
    while True:
        answer = input(
            f'''
Album has been selected!
Do you want to play {ct.prGreen}"{selected_album.name}"{ct.endc} by {ct.prGreen}{selected_album.artists[0].name}{ct.endc}? (Y/N)
If you want to abort type {ct.prRed}"quit"{ct.endc}
''')
        answer = answer.lower()

        if answer == "y":
            print(
                f'\nNow playing {ct.prGreen}"{selected_album.name}"{ct.endc} by {ct.prGreen}{selected_album.artists[0].name}{ct.endc} on Spotify?')

            spotify.playback_start_context(
                tk.to_uri('album', selected_album.id))
            exit()
        elif answer == "n":
            print(f"\n{ct.prLightPurple}Selecting another album...{ct.endc}")
            break
        elif answer == "quit":
            exit()
        else:
            print(
                f"\n{ct.prRed}I didn't understood that. Please try again{ct.endc}")


# Authorization
conf = tk.config_from_file('conf.txt')
token = tk.prompt_for_user_token(
    *conf, scope=tk.scope.user_library_read + tk.scope.user_modify_playback_state)
spotify = tk.Spotify(token)

# Getting the number of all saved albums
albums_number = spotify.saved_albums(limit=1).total
albums = {}

# Checking if the user has any saved albums
if albums_number == 0:
    print(f"\n{ct.prRed}You don't have any saved albums. Aborting!{ct.endc}")
    sleep(2)
    exit()

print(
    f"\nYou have a total of {ct.prGreen}{albums_number}{ct.endc} saved albums. Now selecting one randomly")

# Using function to choose random album. For more info look at the function
while True:
    choosingRandomAlbum(albums_number)
