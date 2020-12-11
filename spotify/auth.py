import requests
import base64
import datetime
client_id="8a8b12a5d08e406e9b676d37884102b1"
client_secret="b67a38ebf65241e9ba6f3ccf83e58b2f"
token_url="https://accounts.spotify.com/api/token"
method="POST"
client_creds=f"{client_id}:{client_secret}"
client_creds_b64=base64.b64encode(client_creds.encode())
token_data={
    "grant_type":"client_credentials"
}
token_headers={
    "Authorization":f"Basic  {client_creds_b64.decode()}"
}
r=requests.post(token_url,data=token_data,headers=token_headers)
valid_request=r.status_code in range(200,299)
if valid_request:
    token_response_data=r.json()
    now=datetime.datetime.now()
    access_token=token_response_data["access_token"]
    expires_in=token_response_data["expires_in"]
    expires=now+datetime.timedelta(seconds=expires_in)
    did_expire=expires<now
