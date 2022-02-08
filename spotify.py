import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
scope = "user-library-read"
client_id = sys.argv[1]
print("Client id : ", client_id)
client_secret = sys.argv[2]
print("Client secret : ", client_secret)
redirect_uri = sys.argv[3]
print("Redirect URI : ", redirect_uri)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
