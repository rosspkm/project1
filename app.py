import os
import flask
from src.main import call_apis

app = flask.Flask(__name__, template_folder='./web/templates', static_folder='./web/static')

artists = ['718COspgdWOnwOFpJHRZHS', '3WrFJ7ztbogyGnTHbHJFl2', '3TVXtAsR1Inumwj472S9r4', '3b8QkneNDz4JHKKKlLgYZg']

@app.route("/")  # Python decorator
def index():
    return flask.render_template("index.html", lst=call_apis(artists=artists))


app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
