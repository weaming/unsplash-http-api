from unsplash.api import Api
from unsplash.auth import Auth

from settings import UNSPLASH_ACCESS_KEY, UNSPLASH_SECRET_KEY

client_id = UNSPLASH_ACCESS_KEY
client_secret = UNSPLASH_SECRET_KEY
# Redirect URI you registered as callback.
redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
# Authorization code to get access token
code = ""

auth = Auth(client_id, client_secret, redirect_uri, code=code)
api = Api(auth)
