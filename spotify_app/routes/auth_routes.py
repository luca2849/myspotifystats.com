import requests, base64, json
from spotify_app.conf.spotify_credentials import *
from spotify_app.util.auth_functions import *
from spotify_app import application
from flask import render_template, url_for, request, redirect, session, flash, g

# ======================= 
# Spotify Authentication
# for tokens, etc.
# =======================

@application.route("/auth/login")
def login():
    return redirect('https://accounts.spotify.com/authorize?response_type=code&client_id=' + credentials["client_id"] + "&scope=" + credentials["scope"] + "&redirect_uri=" + credentials["redirect_url"])

@application.route("/auth/callback")
def callback():
    auth_code = request.args.get('code') # gets the auth code from the URL
    if (auth_code is not None):
        endpoint = 'https://accounts.spotify.com/api/token' # sets the request endpoint
        auth_str = '{}:{}'.format(credentials["client_id"], credentials["client_secret"]) # formats a string with the client ID and client secret
        b64_auth_str = base64.b64encode(auth_str.encode()).decode() # encodes this string
        # sets auth headers for access token request
        headers = {
            "Authorization": "Basic {}".format(b64_auth_str)
        }
        # sets auth data for access token request
        data = {
            "code": auth_code,
            "redirect_uri": credentials["redirect_url"],
            "grant_type": "authorization_code"
        }
        # execute request
        r = requests.post(url=endpoint, headers=headers, data=data)
        r_formatted = json.loads(r.text)
        if (r.status_code == 200):
            # if response was OK (200) set session variables
            session["access_token"] = r_formatted["access_token"]
            session["refresh_token"] = r_formatted["refresh_token"]
            set_user_details()
            return redirect(url_for("home"))
        else:
            return redirect(url_for("login"))
    else:
        return redirect(url_for('auth_error'))

@application.route("/auth/refresh")
def token_refresh():
    success = refresh_access_token()
    if success:
        if "url" in session:
            return redirect(session["url"])
        else:
            return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))

@application.route("/auth/error")
def auth_error():
    return render_template("auth/error.html")
    
@application.route("/auth/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

@application.route("/auth/logcheck")
def logcheck():
    return render_template("auth/logcheck.html", title="Authorization Check")