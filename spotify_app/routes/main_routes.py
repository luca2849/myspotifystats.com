import requests, base64, json
from spotify_app.conf.spotify_credentials import *
from spotify_app.util.auth_functions import *
from spotify_app.util.app_functions import *
from flask import render_template, url_for, request, redirect, session, flash, g
from spotify_app import application

@application.route("/", methods=["GET"])
def home():
    return render_template("index.html", title="Home Page")

@application.route("/app/currently_playing", methods=["GET"])
def currently_playing():
    if request_current_song() is not None:
        resp = request_current_song()
        current = set_current_song_return(resp)
        if current is not None:
            # Either 200 or 204 response code from HTTP request
            return render_template("app/current_song.html", title="Current Song", current=current)
        else:
            # HTTP error when getting current_song
            return render_template("app/error.html", title="Error")           
    else:
        # user is not logged in (has no access token)
        return redirect(url_for('logcheck'))
