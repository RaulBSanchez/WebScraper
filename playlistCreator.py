import spotipy
from spotipy.oauth2 import SpotifyOAuth
import import_ipynb
import pitchfork 
import pandas as pd


best_new_tracks = pitchfork.df2



def get_track_uri(track_title):
    """Searches for a track and returns its URI."""
    print(track_title + " tittle track")
    result = sp.search(q=track_title, type='track', limit=1)
    items = result['tracks']['items']
    if items:
        return items[0]['uri']
    else:
        return None




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