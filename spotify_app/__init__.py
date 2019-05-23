from flask import Flask

# application & SQL Config
application = Flask(__name__)
application.config['SECRET_KEY'] = 'GII5o_Bq3nTEz2TQB0ei9w'
application.config['UPLOAD_FOLDER'] = 'app/static/img'

from spotify_app import routes
