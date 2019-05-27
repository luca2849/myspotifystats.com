import requests, json
from flask import session

def get_user_details():
    if session["access_token"]:
        endpoint = "https://api.spotify.com/v1/me"
        headers = {
            "Authorization": "Bearer " + session["access_token"]
        }
        res = requests.get(url=endpoint, headers=headers)
        if res.status_code != 200:
            return None
        else:
            return res.json()
    else:
        return None

def get_user_playlists():
    if session["access_token"]:
        endpoint = "https://api.spotify.com/v1/me/playlists"
        headers = {
            "Authorization": "Bearer " + session["access_token"]
        }
        res = requests.get(url=endpoint, headers=headers)
        if res.status_code != 200:
            return None
        else:
            return res.json()
    else:
        return None

def get_user_top_tracks(term):
    if session["access_token"]:
        endpoint = "https://api.spotify.com/v1/me/top/tracks"
        headers = {
            "Authorization": "Bearer " + session["access_token"]
        }
        data = {
            "limit": 5,
            "offset": 0,
            "time_range": term
        }
        res = requests.get(url=endpoint, headers=headers, params=data)
        if res.status_code != 200:
            return None
        else:
            return res.json()
    else:
        return None

def get_user_top_artists(term):
    if session["access_token"]:
        endpoint = "https://api.spotify.com/v1/me/top/artists"
        headers = {
            "Authorization": "Bearer " + session["access_token"]
        }
        data = {
            "limit": 5,
            "offset": 0,
            "time_range": term
        }
        res = requests.get(url=endpoint, headers=headers, params=data)
        if res.status_code != 200:
            return None
        else:
            return res.json()
    else:
        return None