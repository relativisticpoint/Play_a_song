import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

# export SPOTIPY_CLIENT_ID='fad493c346d148b9bf130c2e67f65b55'
# export SPOTIPY_CLIENT_SECRET='8b1fd3a82e674964a0addacaa3765ed0'
# export SPOTIPY_REDIRECT_URI='http://localhost:8080'