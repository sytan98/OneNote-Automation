import json
import logging
import yaml
import requests
import msal

logging.basicConfig(filename='history.log',level=logging.DEBUG)

# Load the oauth_settings.yml file
stream = open('oauth_settings.yml', 'r')
settings = yaml.load(stream, yaml.SafeLoader)
print(settings)