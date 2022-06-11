#!/usr/bin/env bash

# Run this script pointing to all libraries required to package them for the Lambda.

terraform init

cp -r /Users/hanruizou/PycharmProjects/sporifyAPI/venv/lib/python3.10/site-packages/spotipy ../lambda_payloads/
cp -r /Users/hanruizou/PycharmProjects/sporifyAPI/venv/lib/python3.10/site-packages/requests ../lambda_payloads/

cp -r /Users/hanruizou/PycharmProjects/sporifyAPI/SpotifyETLpipeline/avg_albums_duration.py ../lambda_payloads/
cp -r /Users/hanruizou/PycharmProjects/sporifyAPI/SpotifyETLpipeline/spotipyLib/get_albums_from_artist.py ../lambda_payloads/spotipyLib/
cp -r /Users/hanruizou/PycharmProjects/sporifyAPI/SpotifyETLpipeline/spotipyLib/get_artists_from_playlist.py ../lambda_payloads/spotipyLib/
cp -r /Users/hanruizou/PycharmProjects/sporifyAPI/SpotifyETLpipeline/spotipyLib/tracks_from_album.py ../lambda_payloads/spotipyLib/

cd ../lambda_payloads/

zip -r ../../payload.zip *

cd ../tf/

terraform plan
