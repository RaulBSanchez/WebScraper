import spotipy
from spotipy.oauth2 import SpotifyOAuth
import import_ipynb
import pitchfork 
import pandas as pd
import pprint


best_new_tracks = pitchfork.df2

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="a83a09741adc4b788ba382acc6fcdb09",
                                               client_secret="9f0ebe92048b42ef9df2b05c623e5b8f",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-library-read playlist-modify-public",
                                               ))


user_id = sp.me()["id"]
playlist_name = "test"
'''
def get_track_uri(track_title):
    """Searches for a track and returns its URI."""
    print(track_title + " tittle track")
    result = sp.search(q=track_title, type='track', limit=1)
    items = result['tracks']['items']
    if items:
        return items[0]['uri']
    else:
        return None
'''

def create_playlist():
    #user = raulbazan11
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, collaborative=False, description='test')
    pprint.pprint(playlist)
    #print(playlist)
    #playlist_id = playlist["id"]
    #sp.playlist_add_items(playlist["id"], ["0V8TG3xjxM9IrBK2EMrCny"], position=None )

create_playlist()

'''
def bestnewsongs(best_new_tracks):

    track_uris = []

    for index, row in best_new_tracks.iterrows():
        artist = row['Artist']
        track = row['Track']
        query = (f"Artist: {artist}, Track: {track}")

    
        track_uri = get_track_uri(query)
        if track_uri:
            #print(f"Artist: {artist}, Track: {track}, URI: {track_uri}")
            best_new_tracks
            track_uris.append(track_uri)

        else:
            print(f"Could not find URI for '{track}' by {artist}")

    best_new_tracks['Track_URI'] = track_uris
bestnewsongs(best_new_tracks)

print(best_new_tracks)
'''