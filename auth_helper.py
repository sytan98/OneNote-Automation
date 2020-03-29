import yaml
from requests_oauthlib import OAuth2Session
import os
import time

print("test")


# Load the oauth_settings.yml file
stream = open('oauth_settings.yml', 'r')
settings = yaml.load(stream, yaml.SafeLoader)
print(settings)

authorize_url = '{0}{1}'.format(settings['authority'], settings['authorize_endpoint'])
print(authorize_url)
token_url = '{0}{1}'.format(settings['authority'], settings['token_endpoint'])
print(token_url)



# Method to exchange auth code for access token
def get_token_from_code(callback_url, expected_state):
  # Initialize the OAuth client
  aad_auth = OAuth2Session(settings['app_id'],
    state=expected_state,
    scope=settings['scopes'],
    redirect_uri=settings['redirect'])

  token = aad_auth.fetch_token(token_url,
    client_secret = settings['app_secret'],
    authorization_response=callback_url)

  return token