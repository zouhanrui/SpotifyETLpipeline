import requests

GET_PLAYLIST_URL = 'https://api.spotify.com/v1/playlists'
PLAYLIST_ID = '37i9dQZF1EJGp4oDkQP4ga'
ACCESS_TOKEN = 'BQA-k8YFTMeAimG-t0XI8h4q6APFuXgft2gmLtIzDjJpjEU1m7Tyh4ecb-clD2DV6gnuSDL7V6DaJr-8ipdIJ5o7nxatLCXdLKKprRDXhYDzj8mHb7a_k3E8ua7zTbjComQM9EGAO3nDsJOMh8oh7zHflpeTeVEeeVN60RoasUzeTd1_6PULhfMkmGSG96XR972zU4ZNenYhBHdkvtUkWNKucCnzupwT'

def get_playlist_from_spotify(playlist_id):
    response = requests.get(
        GET_PLAYLIST_URL + '/' + playlist_id,
        headers={
            'Authorization': f"Bearer {ACCESS_TOKEN}",
            'Content-Type': 'application/json'
        }
    )

    return response.json()


def main():
    response = get_playlist_from_spotify(
        playlist_id=PLAYLIST_ID
    )
    print("fuck you")
    print(response)


if __name__ == '__main__':
    main()
