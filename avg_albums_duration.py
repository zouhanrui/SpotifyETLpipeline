import csv
from datetime import datetime
import os

os.environ['SPOTIPY_CLIENT_ID'] = ''
os.environ['SPOTIPY_CLIENT_SECRET'] = ''

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

import boto3
from awsboto3.boto3_s3_functions import upload_file, \
    list_buckets, \
    list_objects_from_bucket

from spotipyLib.get_albums_from_artist import get_albums_from_artist
from spotipyLib.get_artists_from_playlist import get_artists_from_playlists
from spotipyLib.tracks_from_album import get_tracks_from_album

s3_client = boto3.client('s3')

PLAYLIST_URL = 'spotify:playlist:3EuBX91Ew2WBaL2hvLCs32'

playlist = spotify.playlist(PLAYLIST_URL)
playlist_name = playlist['name']
artists = get_artists_from_playlists(playlist_url=PLAYLIST_URL)


def get_avg_album_duration():
    final_data_dictionary = {
        'Release_date': [],
        'Album name': [],
        'Artist name': [],
        'Total Track': [],
        'Total duration_ms': []
    }

    with open(f'data/{playlist_name}.csv', 'w') as file:
        header = final_data_dictionary.keys()
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()

        for artist in artists:
            # print(artist)
            artist_uri = artists[artist]
            artist_albums = get_albums_from_artist(artist_id=artist_uri)
            # print(artist_albums)
            for album_name in artist_albums:
                print(album_name + '\n')
                total_duration_this_album = 0
                album = artist_albums[album_name]
                album_uri = album['album_uri']
                # print('------------------------------------------------')
                tracks = get_tracks_from_album(album_uri)
                # print('------------------------------------------------')
                # print(len(tracks))
                total_tracks = len(tracks)
                for track_name in tracks:
                    track = tracks[track_name]
                    total_duration_this_album += track['duration_ms']
                # print(total_duration_this_album / len(tracks))
                # print(album)
                writer.writerow({
                    'Release_date': album['release_date'],
                    'Album name': album_name,
                    'Artist name': artist,
                    'Total Track': total_tracks,
                    'Total duration_ms': total_duration_this_album
                })
                final_data_dictionary['Release_date'].append(album['release_date'])
                final_data_dictionary['Album name'].append(album_name)
                final_data_dictionary['Artist name'].append(artist)
                final_data_dictionary['Total Track'].append(total_tracks)
                final_data_dictionary['Total duration_ms'].append(total_duration_this_album)

    return final_data_dictionary


def load_data_s3():
    final_data_dictionary = get_avg_album_duration()
    # print(final_data_dictionary)

    # boto3 s3 sdk
    """
    buckets = list_buckets()
    all_objects_by_bucket = {}
    for bucket in buckets:
        objects = list_objects_from_bucket(bucket_name=bucket)
        all_objects_by_bucket[bucket] = objects
    print('List all objects from all s3 buckets:\n ' + str(all_objects_by_bucket))
    """

    # Upload csv to s3
    date = datetime.now()
    bucket_name = 'spotify-project-data'
    file_path = f'data/{playlist_name}.csv'
    key = f'{date.year}/{date.month}/{date.day}/{playlist_name}.csv'
    upload_file(file_path=file_path, bucket_name=bucket_name, key=key)


def lambda_handler(event, context):
    load_data_s3()


def main():
    load_data_s3()

    # return final_data_dictionary


if __name__ == '__main__':
    main()
