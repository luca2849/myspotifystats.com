import requests, json
from flask import session
from spotify_app.conf.spotify_credentials import *

def refresh_access_token():
    '''
    Function to use the users refresh token
    to get a new access token when it expires
    '''
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

def set_user_details():
    '''
    Function for setting the user's details
    for use in the session, and for creating
    elements such as the name and image at the
    top right
    '''
    if session.get("access_token"):
        endpoint = 'https://api.spotify.com/v1/me'
        headers = {
            "Authorization": "Bearer " + session["access_token"]
        }
        resp = requests.get(url=endpoint, headers=headers)
        if (resp.status_code == 200):
            res = resp.json()
            session["firstname"] = res["display_name"].split()[0]
            session["name"] = res["display_name"]
            if (len(res["images"]) == 0):
                session["profile_img"] = "http://www.myspotifystats.com/default.png"
            else:
                session["profile_img"] = res["images"][0]["url"]
            return True
        else:
            return False
    else:
        return False