import os
import flask
from src.main import call_apis
app = flask.Flask(__name__, template_folder='./web/templates', static_folder='./web/static')

artists = ['718COspgdWOnwOFpJHRZHS', '3WrFJ7ztbogyGnTHbHJFl2', '3TVXtAsR1Inumwj472S9r4', '3b8QkneNDz4JHKKKlLgYZg', '7dGJo4pcD2V6oG8kP0tJRR', '55Aa2cqylxrFIXC767Z865', '4r63FhuTkUYltbVAg5TQnk', '6yJCxee7QumYr820xdIsjo']

@app.route("/")  # Python decorator
def index():
    return flask.render_template("index.html", lst=call_apis(artists=artists))


app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 4141)),
    debug=True
)
