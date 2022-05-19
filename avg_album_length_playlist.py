#import spotipy
#import csv
#import boto3
#from datetime import datetime

#from config.playlists import spotify_playlists

#spotipy_object = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())

final_data_dictionary = {
    'Year Released': [],
    'Album Length': [],
    'Album Name': [],
    'Artist': []
}

PLAYLIST = 'Eminem - Recovery'


def gather_data_local():
    return final_data_dictionary


if __name__ == '__main__':
    data = gather_data_local()
