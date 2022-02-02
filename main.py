import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-recently-played"
client_id = sys.argv[1]
print("Client id : ", client_id)
client_secret = sys.argv[2]
print("Client secret : ", client_secret)
redirect_uri = sys.argv[3]
print("Redirect URI : ", redirect_uri)


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))


result = sp.current_user_recently_played(limit=50, after=None, before=None)
# print(result)
for idx, item in enumerate(result['items']):
    track = item['track']
    print(idx, track['name'])

