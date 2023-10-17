#!/usr/bin/env python3

from playlist_generator import SpotifyPlaylist, separator


if __name__ == '__main__':
    
    print(separator)
    print(' SPOTIFY PLAYLIST GENERATOR '.center(100, '-'))
    print(separator)

    while True:
        prompt = input('Playlist Prompt: ')
        if prompt:
            break
        else:
            print('Invalid Answer. Prompt cannot be empty.')
    
    while True:
        length = input('Playlist/Batch Length: ')
        if length.isdigit():
            if int(length) > 0:
                break
        print('Invalid length. Please enter a positive integer.')
    
    name = input('Playlist Name (leave blank to use prompt): ')
    if not name:
        name = prompt

    while True:
        match input('Interactive Mode? [y]es or [n]o: '):
            case 'y':
                interactive = True
                break
            case 'n':
                interactive = False
                break
            case _:
                print("Invalid answer. Please enter 'y' or 'n'")

    print('Creating playlist. Please wait...')
    playlist = SpotifyPlaylist(prompt, length, name, interactive)
    playlist.main()
    print(playlist)