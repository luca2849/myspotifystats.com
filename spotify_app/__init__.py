from flask import Flask

# application & SQL Config
application = Flask(__name__)
application.config['SECRET_KEY'] = 'GII5o_Bq3nTEz2TQB0ei9w'
application.config['UPLOAD_FOLDER'] = 'app/static/img'
application.config.update(dict(
  PREFERRED_URL_SCHEME = 'https'
))

from spotify_app.routes import auth_routes
from spotify_app.routes import main_routes
from spotify_app.routes import user_routes
from spotify_app.routes import app_routes
