import requests, base64, json
from spotify_app.conf.spotify_credentials import *
from spotify_app.util.auth_functions import *
from flask import render_template, url_for, request, redirect, session, flash, g
from spotify_app import application

@application.route("/", methods=["GET"])
def home():
    print(session)
    return render_template("index.html", title="Home Page")
