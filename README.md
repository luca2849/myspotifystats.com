# myspotifystats.com

## Info
MySpotifyStats.com is a small app written using Python Flask, Jinja2 tamplating, HTML, CSS and JavaScript.
It allows users to sign in through Spotify, and view their top tracks and artists from the last 4 weeks,
6 months and from all of Spotify's data. Users can also check what is currently playing and what has
recently played to completion.

## Security Info
In the interest of security a file (spotify_credentials.py) which contained a dictionary of API keys and callback urls, etc. has
been removed from this repository.

## spotify_credentials.py Syntax
Place this file in ./spotify_app/conf/spotify_credentials.py
```py
credentials = {
  "client_id": '<Your Client ID>',
  "client_secret": '<Your Client Secret>',
  "scope": '<Your Scope>',
  "redirect_url": '<Your Redirect URL Route>'
}
```
