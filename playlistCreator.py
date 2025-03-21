import spotipy
from spotipy.oauth2 import SpotifyOAuth
import import_ipynb
import pitchfork 
import pandas as pd
import pprint
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 

best_new_tracks = pitchfork.df2


client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id,
                                               client_secret,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-library-read playlist-modify-public"))

# Get URI of my username
user_id = sp.me()["id"]
playlist_name = "testing"


def get_track_uri(track_title):
    """Searches for a track and returns its URI."""
    
    result = sp.search(q=track_title, type='track', limit=1)
    items = result['tracks']['items']
    #pprint.pprint(items)
    
    
    if items:
        return items[0]['uri']
        
    else:
        return None
    


def create_playlist():
    
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, collaborative=False, description='test')
    #pprint.pprint(playlist)
    #print(playlist)
    playlist_id = playlist["id"]
    #sp.playlist_add_items(playlist["id"], ["spotify:track:0V8TG3xjxM9IrBK2EMrCny"], position=None )
    return playlist_id

playlist_id = create_playlist()
#bestnewsongs(best_new_tracks, playlist_id)
print(playlist_id + " this is the playlist id")

def add_songs(track_uri, playlist_id):
    # have to get the URI from best_new_tracks['Track_URI'] = track_uris
    # iterate through the list and add the songs to the playlist
    #print(track_uri, playlist_id)
    sp.playlist_add_items(playlist_id, [track_uri], position=None )


def bestnewsongs(best_new_tracks, playlist_id):
    track_uris = []

    for index, row in best_new_tracks.iterrows():
        artist = row['Artist']
        track = row['Track']
        query = (f"Artist: {artist}, Track: {track}")

    
        track_uri = get_track_uri(query)
        if track_uri:
            #print(f"Artist: {artist}, Track: {track}, URI: {track_uri}")
            add_songs(track_uri, playlist_id)
            #track_uris.append(track_uri)

        else:
            print(f"Could not find URI for '{track}' by {artist}")

    #best_new_tracks['Track_URI'] = track_uris

bestnewsongs(best_new_tracks, playlist_id)

