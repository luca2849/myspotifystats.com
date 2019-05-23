from flask import session
import requests

def request_current_song():
    if (session.get("access_token")):
        endpoint = 'https://api.spotify.com/v1/me/player/currently-playing'
        headers = {
            "Authorization": "Bearer " + session["access_token"]
        }
        return requests.get(url=endpoint, headers=headers)
    else:
        return None
