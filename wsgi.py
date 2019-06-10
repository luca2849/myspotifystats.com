#! /usr/bin/python
import sys

sys.path.insert(0,"/var/www/myspotifystats.com/")

from spotify_app import application

if __name__ == '__main__':
    application.run(debug=True)
