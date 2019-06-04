import json
from spotify_app import application
from flask import render_template, url_for, redirect, session
from spotify_app.util.app_functions import request_current_song, set_current_song_return, get_recently_played

# Route for getting the user's currently playing song (if any)
@application.route("/app/currently_playing", methods=["GET"])
def currently_playing():
    if request_current_song() is not None:
        # HTTP response for current users song
        resp = request_current_song()
        # Function for setting what is seen in the views
        # with the current variable
        current = set_current_song_return(resp)
        recent = get_recently_played()
        if current and recent is not None:
            # Either 200 (success) or 204(success but no content) response code from HTTP request
            print(json.loads(recent.text)["items"][0]["track"]["name"])

            return render_template("app/current_song.html", title="Current Song", current=current, recent=json.loads(recent.text)["items"])
        else:
            session["url"] = url_for("currently_playing")
            # HTTP error when getting current_song
            return redirect(url_for('app_error'))          
    else:
        # user is not logged in (has no access token)
        return redirect(url_for('logcheck'))

# Route for an error in the application flow
@application.route("/app/error", methods=["GET"])
def app_error():
    return render_template('app/error.html', title="Application Error")