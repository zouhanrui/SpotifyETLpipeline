import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

os.environ['SPOTIPY_CLIENT_ID'] = ''
os.environ['SPOTIPY_CLIENT_SECRET'] = ''

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

ALBUM_ID = 'spotify:album:1JvoMzqg04nC29gam4Qaiq'


def get_tracks_from_album(album_id):
    tracks = {}
    album_data = spotify.album(album_id)
    for item in album_data['tracks']['items']:
        duration_ms = item['duration_ms']
        track_name = item['name']
        track_uri = item['uri']

        tracks[track_name] = {}
        tracks[track_name]["duration_ms"] = duration_ms
        tracks[track_name]["track_uri"] = track_uri

    print(tracks)
    return tracks


def main():
    tracks = get_tracks_from_album(album_id=ALBUM_ID)
    return tracks


if __name__ == '__main__':
    main()