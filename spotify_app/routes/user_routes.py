from datetime import datetime
from spotify_app import application
from flask import render_template, url_for, redirect, session
from spotify_app.util.user_functions import get_user_details, get_user_playlists, get_user_top_tracks

@application.route("/user/profile", methods=["GET"])
def profile():
    # Check if logged in, show user page
    if "access_token" in session:
        # Request user details and store
        user_details = get_user_details()
        # Request playlist details
        user_playlists = get_user_playlists()
        # Request top artists, genres and songs
        long_user_top_tracks = get_user_top_tracks("long_term")
        med_user_top_tracks = get_user_top_tracks("medium_term")
        short_user_top_tracks = get_user_top_tracks("short_term")
        if (user_details != None and user_playlists != None and long_user_top_tracks != None):
            # Format date
            bdate = user_details["birthdate"]
            formatted = datetime.strptime(bdate, '%Y-%m-%d')
            formatted = formatted.strftime('%m/%d/%Y')
            return render_template("user/profile.html", title="Your Profile", user_details=user_details, user_playlists=user_playlists["items"], med_user_top_tracks=med_user_top_tracks["items"], short_user_top_tracks=short_user_top_tracks["items"], long_user_top_tracks=long_user_top_tracks["items"], birthdate=formatted)
        else:
            return redirect(url_for("token_refresh"))
    else:
        return redirect(url_for("login"))