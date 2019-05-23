import requests, json
from flask import session
from spotify_app.conf.spotify_credentials import *

def refresh_access_token():
    if (session["refresh_token"]):
        endpoint = "https://accounts.spotify.com/api/token"
        data = {
            "client_id": credentials["client_id"],
            "client_secret": credentials["client_secret"],
            "grant_type": 'refresh_token',
            "refresh_token": session["refresh_token"]
        }
        r = requests.post(url=endpoint, data=data)
        r_formatted = json.loads(r.text)
        new_token = r_formatted["access_token"]
        session.pop('access_token', None)
        session["access_token"] = new_token
        return True
    else:
        return False