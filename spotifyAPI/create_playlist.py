import requests

SPOTIFY_CREATE_PLAYLIST_URL = 'https://api.spotify.com/v1/users/buo16x8c8u1qq4bfkj3wbn1ow/playlists'
ACCESS_TOKEN = 'BQBvjF_fQEAoYh1Fe3E2FUhxIuSdIMgsaNQwbOHWVH96WSnzlgTbmK-bXPFxjHt4z5MNKOXGGRHByVmMnkDN8S2C6OzyDEGIKM6UjKp0RKLBrR1ODNapQNrw2peJ1Nz8Vy7O-j7gvHxu1JEaLJwH9YqVFtN5xCfVxi_dh8H0Oz29ncZNr3-oUrVqLofXfzuDcxmlJcK1ZE8m735GvRa5uAi39LCPb0_d'


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
