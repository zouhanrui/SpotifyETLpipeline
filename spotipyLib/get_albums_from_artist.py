import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials

os.environ['SPOTIPY_CLIENT_ID'] = ''
os.environ['SPOTIPY_CLIENT_SECRET'] = ''

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

artist_id = '1uNFoZAHBGtllmzznpCI3s'


def get_albums_from_artist(artist_id):
    #flag = 1
    artist_albums = {}
    albums = spotify.artist_albums(artist_id=artist_id, limit=10)
    for item in albums['items']:
        album_name = item['name']
        release_date = item['release_date']
        total_tracks = item['total_tracks']
        album_uri = item['uri']
        # available_markets = item['available_markets']

        # if album name is the duplicated, overwrite
        artist_albums[album_name] = {}
        #artist_albums[album_name]["flag"] = flag
        artist_albums[album_name]["release_date"] = release_date
        artist_albums[album_name]["total_tracks"] = total_tracks
        artist_albums[album_name]["album_uri"] = album_uri
        # artist_albums[album_name]["available_markets"] = available_markets
        #flag += 1

    #print(artist_albums.keys())
    #print(artist_albums)

    return artist_albums


def main():
    albums = get_albums_from_artist(artist_id)


if __name__ == '__main__':
    main()
