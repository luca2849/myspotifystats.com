from flask import session, url_for
import requests

def request_current_song():
	'''
		HTTP request for the currently playing song
		for a user's spotify
	'''
	if (session.get("access_token")):
		endpoint = 'https://api.spotify.com/v1/me/player/currently-playing'
		headers = {
			"Authorization": "Bearer " + session["access_token"]
		}
		return requests.get(url=endpoint, headers=headers)
	else:
		return None

def set_current_song_return(resp):
	'''
		Function used to choose what to return
		to the user for their current song, depending
		if a song is playing or not
	'''
	if (resp.status_code == 200):
		res = resp.json()["item"]
		current = {
			"name": res["name"],
			"img": res["album"]["images"][0]["url"],
			"album": res["album"]["name"],
			"release": '(' + res["album"]["release_date"][0:4] + ')',
			"artist": res["artists"][0]["name"]
		}
		return current
	elif (resp.status_code == 204):
		current = {
			"name": "No Song Playing",
			"img": url_for('static', filename='img/pikachu.png'),
			"album": "To have a song show here, start one on your spotify",
			"release": "",
			"artist": ""
		}
		return current
	else:
		return None

