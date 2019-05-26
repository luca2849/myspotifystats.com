from flask import render_template
from spotify_app import application

@application.route("/", methods=["GET"])
def home():
    return render_template("index.html", title="Home Page")
