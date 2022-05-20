import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

os.environ['SPOTIPY_CLIENT_ID'] = ''
os.environ['SPOTIPY_CLIENT_SECRET'] = ''

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials()) # <spotipy.client.Spotify object at 0x10a973940>
'''
print(spotify)
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
'''
#playlists = spotify.user_playlists('spotify')
#print(playlists['items'])
'''
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = spotify.next(playlists)
    else:
        playlists = None
'''

artist_id = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
artist = spotify.artist(artist_id)
#print(artist)

user = spotify.user('Hanrui')
#print(user)

playlist_id = 'spotify:playlist:0ldNWi8AMzxJUFI8eCzBTe'
playlist = spotify.playlist(playlist_id)
#print(playlist)

album_id = 'spotify:album:1JvoMzqg04nC29gam4Qaiq'
album = spotify.album(album_id)
print(len(album['tracks']['items']))

playlist_tracks = spotify.playlist_tracks(playlist_id=playlist_id)
#print(playlist_tracks)

artist_id = 'spotify:artist:1uNFoZAHBGtllmzznpCI3s'
artist_albums = spotify.artist_albums(artist_id=artist_id, limit=10)
#print(artist_albums)
