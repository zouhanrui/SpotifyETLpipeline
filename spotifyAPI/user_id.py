import access_token

import requests

URL = 'https://api.spotify.com/v1/me'
ACCESS_OAUTH_TOKEN = access_token.get_access_token()


# print(ACCESS_OAUTH_TOKEN)


def get_user_id(access_oauth_token):
    response = requests.get(
        URL,
        headers={
            'Authorization': f'Bearer {access_oauth_token}',
            'Content-Type': 'application/json'
        }
    )
    return response.json()['id']


def main():
    user_id = get_user_id(access_oauth_token=ACCESS_OAUTH_TOKEN)
    print(user_id)


if __name__ == '__main__':
    main()
