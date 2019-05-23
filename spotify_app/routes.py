import requests, base64, json
from spotify_app.conf.spotify_credentials import *
from flask import render_template, url_for, request, redirect, session, flash, g
from spotify_app import application

@application.route("/", methods=["GET"])
def home():
    print(session)
    return render_template("index.html", title="Home Page")

# ======================= 
# Spotify Authentication
# for tokens, etc.
# =======================

@application.route("/auth/login")
def login():
    return redirect('https://accounts.spotify.com/authorize?response_type=code&client_id=' + credentials["client_id"] + "&scope=" + credentials["scope"] + "&redirect_uri=" + credentials["redirect_url"])

@application.route("/auth/callback")
def callback():
    auth_code = request.args.get('code')
    endpoint = 'https://accounts.spotify.com/api/token'
    auth_str = '{}:{}'.format(credentials["client_id"], credentials["client_secret"])
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()
    headers = {
        "Authorization": "Basic {}".format(b64_auth_str)
    }
    data = {
        "code": auth_code,
        "redirect_uri": credentials["redirect_url"],
        "grant_type": "authorization_code"
    }
    r = requests.post(url=endpoint, headers=headers, data=data)
    r_formatted = json.loads(r.text)
    if (r_formatted.get("access_token")):
        session["access_token"] = r_formatted["access_token"]
        session["refresh_token"] = r_formatted["refresh_token"]
        return redirect(url_for("home"))
    else:
        return redirect(url_for("auth_error"))

@application.route("/auth/error")
def auth_error():
    return render_template("auth/error.html")
    
