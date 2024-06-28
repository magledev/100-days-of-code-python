# Spotify playlist creator via Billboard Hot 100 chart for a given date.

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Billboard Implementation.
BB_ENDPOINT = "https://www.billboard.com/charts/hot-100/"
# Get Billboard Hot 100 data
bb_date = input("What date would you like to create a playlist for? (YYYY-MM-DD): ")
response = requests.get(url=f"{BB_ENDPOINT}{bb_date}")
bb_data = response.text

# Use BeautifulSoup to scrape useful webpage info.
soup = BeautifulSoup(bb_data, 'html.parser')
raw_titles = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
raw_artists = soup.find_all(name="span", class_="a-no-trucate")
titles = [title.getText().strip('\n\t') for title in raw_titles]
artists = [artist.getText().strip('\n\t') for artist in raw_artists]
top_100_list = [f"{artist} - {title}" for artist, title in zip(artists, titles)]

# Use Spotipy to search and then create playlist for current user.
sp_scope = 'playlist-modify-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=sp_scope))

def spotify_search():
    year = bb_date.split("-")[0]
    song_uris = []
    for song in titles:
        sp_search = sp.search(q=f"track:{song} year:{year}", type="track")
        print(sp_search)
        try:
            uri = sp_search["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} does not exist. Skipped")
    return(song_uris)

def spotify_playlist_create(song_uris):
    sp_user = sp.current_user()
    sp_pl_name = input("Enter Playlist Name: ")
    sp_pl_desc = input("Enter Playlist Description: ")
    top_100_pl = sp.user_playlist_create(sp_user["id"], sp_pl_name, public=False, collaborative=False, description=sp_pl_desc)
    top_100_pl_id = top_100_pl["id"]
    sp.playlist_add_items(playlist_id=top_100_pl_id, items=song_uris, position=None)
    print(song_uris)
    print(f"Found and added {len(song_uris)}/{len(top_100_list)} possible tracks.")

spotify_playlist_create(spotify_search())
