import yaml
import msal
import logging
from datetime import datetime

# Method to exchange auth code for access token
def get_token(settings):
  dateTimeObj = datetime.now()
  timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")

  authorize_url = '{0}{1}'.format(settings['authority'], settings['app_id'])
  logging.info("{}: Authorize URL is {}".format(timestampStr ,authorize_url))
  app = msal.PublicClientApplication(settings['client_id'], authority = authorize_url)
  # Initialize the OAuth client
  try:
    token = app.acquire_token_by_username_password(settings['username'], 
                                                   settings['password'], 
                                                   scopes=settings['scope'])
    logging.info("{}: Token is {}".format(timestampStr ,token))                                               
  except:
    logging.exception("{}: Could not get token".format(timestampStr))

  return token