import requests
import base64
import datetime
client_id="8a8b12a5d08e406e9b676d37884102b1"
client_secret="b67a38ebf65241e9ba6f3ccf83e58b2f"

class SpotifyApi(object):
    access_token=None
    access_token_expires=datetime.datetime.now()
    access_token_did_expire=True
    client_id=None
    client_secret=None
    token_url="https://accounts.spotify.com/api/token"

    def __init__(self,client_id,client_secret):
        super().__init__()
        self.client_id=client_id
        self.client_secret=client_secret
    def get_client_Credentials(self):
        client_id=self.client_id
        client_secret=self.client_secret
        if client_id==None or client_secret==None:
            raise Exception("You must set a Client id and Client secret")
        client_creds=f"{client_id}:{client_secret}"
        client_creds_b64=base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()

    def get_token_headers(self):
        client_creds_b64=self.get_client_Credentials()
        return {
                    "Authorization":f"Basic  {client_creds_b64}"
                }
    def get_token_data(self):
        return {
                    "grant_type":"client_credentials"
                }

    def perform_auth(self):
        token_url=self.token_url
        token_data=self.get_token_data()
        token_headers=self.get_token_headers()
        r = requests.post(token_url, data=token_data, headers=token_headers)
        if r.status_code not in range(200, 299):
            return False
        data = r.json()
        now = datetime.datetime.now()
        access_token = data["access_token"]
        expires_in = data["expires_in"]
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token_expires=expires
        self.access_token_did_expire= expires < now
        print("self.acc",self.access_token_expires)
        print("expires",expires)
        print("expires_in",expires_in)
        return True

spotify=SpotifyApi(client_id,client_secret)