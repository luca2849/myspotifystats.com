from flask import Flask

# application & SQL Config
application = Flask(__name__)
application.config['SECRET_KEY'] = 'GII5o_Bq3nTEz2TQB0ei9w'
application.config['UPLOAD_FOLDER'] = 'app/static/img'
application.config.update(dict(
  PREFERRED_URL_SCHEME = 'https'
))
def _force_https():
    # my local dev is set on debug, but on AWS it's not (obviously)
    # I don't need HTTPS on local, change this to whatever condition you want.
    if not application.debug: 
        from flask import _request_ctx_stack
        if _request_ctx_stack is not None:
            reqctx = _request_ctx_stack.top
            reqctx.url_adapter.url_scheme = 'https'

application.before_request(_force_https)

from spotify_app.routes import auth_routes
from spotify_app.routes import main_routes
from spotify_app.routes import user_routes
from spotify_app.routes import app_routes
