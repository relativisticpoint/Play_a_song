
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

# export SPOTIPY_CLIENT_ID='1b27856640e94ce4b1a1c516a44695e9'
# export SPOTIPY_CLIENT_SECRET='ae2f3f4e824448e3898e3f11d1ce106c'
# export SPOTIPY_REDIRECT_URI= "https://localhost:9090"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])