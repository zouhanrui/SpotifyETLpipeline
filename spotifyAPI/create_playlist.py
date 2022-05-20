import requests

SPOTIFY_CREATE_PLAYLIST_URL = 'https://api.spotify.com/v1/users/buo16x8c8u1qq4bfkj3wbn1ow/playlists'
ACCESS_TOKEN = ''

def create_playlist_on_spotify(name, public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json={
            "name": name,
            "public": public
        }
    )
    json_resp = response.json()

    return json_resp


def main():
    playlist = create_playlist_on_spotify(
        name="webAPI",
        public=False
    )

    print(f"Playlist: {playlist}")


if __name__ == '__main__':
    main()
