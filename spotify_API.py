import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

# Set up Spotify API credentials
load_dotenv()
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

# Authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    songs = [item['track']['name'] + ' by ' + item['track']['artists'][0]['name'] for item in tracks]
    return songs

# #Example usage:
# playlist_id = '3HvgaZeBWbr7UjFeicPFRI'
# song_names = get_playlist_tracks(playlist_id)
# print(song_names)
