import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

os.environ['SPOTIPY_CLIENT_ID'] = ''
os.environ['SPOTIPY_CLIENT_SECRET'] = ''

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

playlist_id = 'spotify:playlist:0ldNWi8AMzxJUFI8eCzBTe'

LIMIT = 10

def get_artists_from_playlists(playlist_url):
    playlist_tracks = spotify.playlist_tracks(playlist_id=playlist_url, limit=LIMIT)
    artists = {}
    for song in playlist_tracks['items']:
        track = song['track']
        artist = track['artists'][0]['name']
        artist_uri = track['artists'][0]['uri']
        artists[artist_uri] = artist
    print(artists)
    return artists





def main():
    get_artists_from_playlists(playlist_url=playlist_id)


if __name__ == '__main__':
    main()

