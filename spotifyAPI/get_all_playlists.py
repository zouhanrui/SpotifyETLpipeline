import requests
import user_id
import access_token

ACCESS_OAUTH_TOKEN = access_token.get_access_token()
USER_ID = user_id.get_user_id(access_oauth_token=ACCESS_OAUTH_TOKEN)
LIMIT = 10


def get_all_playlists(user_id, limit):
    response = requests.get(
        f'https://api.spotify.com/v1/users/{user_id}/playlists?limit={limit}',
        headers={
            'Authorization': f'Bearer {ACCESS_OAUTH_TOKEN}',
            'Content-Type': 'application/json'
        }
    )
    return response.json()


def main():
    response = get_all_playlists(user_id=USER_ID, limit=LIMIT)
    my_playlist = {}
    for i in range(LIMIT):
        playlist_name = response['items'][i]['name']
        playlist_tracks_count = response['items'][i]['tracks']['total']
        my_playlist[playlist_name] = playlist_tracks_count
    print(my_playlist)


if __name__ == '__main__':
    main()
