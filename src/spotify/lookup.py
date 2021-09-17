from src.spotify.lib.functions import get_data

def find_author(token, authors=None):
    """
    Function to get data from spotify api
    """
    return_dict = {}

    for author in authors:

        data = get_data(
            url=f"https://api.spotify.com/v1/artists/{author}/top-tracks?market=US",
            headers={"Authorization": f"Bearer {token}"}
        )

        for i in data['tracks']:
            artist = i['artists'][0]['name']

            if not artist in return_dict:
                return_dict[artist] = {}

            art = i['album']['images'][0]['url']
            song_name = i['name']
            song_url = i['preview_url']
            return_dict[artist][song_name] = {
                'image': art,
                'song_url': song_url
            }
    return return_dict