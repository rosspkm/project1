from dotenv import find_dotenv, load_dotenv
from src.spotify.lib.classes import Spotify_Auth
from src.spotify.lookup import find_author
from src.genius.lookup import find_genius_link

load_dotenv(find_dotenv())
auth = Spotify_Auth()


def call_apis(artists):
    
    return find_genius_link(find_author(token=auth.access_token, authors=artists))
