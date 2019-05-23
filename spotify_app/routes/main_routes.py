import requests, base64, json
from spotify_app.conf.spotify_credentials import *
from spotify_app.util.auth_functions import *
from flask import render_template, url_for, request, redirect, session, flash, g
from spotify_app import application

@application.route("/", methods=["GET"])
def home():
    print(session)
    return render_template("index.html", title="Home Page")

@application.route("/app/currently_playing", methods=["GET"])
def currently_playing():
    print(session)
    if (session.get("access_token")):
        endpoint = 'https://api.spotify.com/v1/me/player/currently-playing'
        headers = {
            "Authorization": "Bearer " + session["access_token"]
        }
        resp = requests.get(url=endpoint, headers=headers)
        if (resp.status_code == 200):
            res = resp.json()["item"]
            current = {
                "name": res["name"],
                "img": res["album"]["images"][0]["url"],
                "album": res["album"]["name"],
                "release": '(' + res["album"]["release_date"][0:4] + ')',
                "artist": res["artists"][0]["name"]
            }
            return render_template("app/current_song.html", title="Current Song", current=current)
        elif (resp.status_code == 204):
            # no song is playing
            current = {
                "name": "No Song Playing",
                "img": url_for('static', filename='img/pikachu.png'),
                "album": "",
                "release": "",
                "artist": ""
            }
            return render_template("app/current_song.html", title="Current Song", current=current)
        else:
            return "Error"
    return "HEllo"