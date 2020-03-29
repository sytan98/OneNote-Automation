import json
import logging
import yaml
import requests
import msal
import codecs
from requests_toolbelt import MultipartEncoder
import pprint

api_endpoint2 = "https://graph.microsoft.com/v1.0/me/onenote/sections/1-5845c339-3ede-4f2c-8883-8e7184fca495/pages"
files = {'file': ('test.html', open('test.html', 'rb'))}
headers={'Authorization': 'Bearer ' + result['access_token'], "content-type": "text/html"}

body = '''
    <!DOCTYPE html>
    <html>
      <head>
        <title>Testing</title>
        <meta name="created" content="2015-07-22T09:00:00-08:00" />
      </head>
      <body>
        <p>Here's a file attachment:</p>
        <img data-render-src="name:fileBlock1" />
        <object data-attachment="lecture15(1).pdf" data="name:fileBlock1" type="application/pdf" />
      </body>
    </html>
    '''
fin = open('lecture15(1).pdf', 'rb')
# files = {'name': (<filename>, <file object>, <content type>, <per-part headers>)}
files = {'presentation': (None, body, 'text/html'),
        'fileBlock1': (None, fin, 'application/pdf')}


headers={'Authorization': 'Bearer ' + result['access_token']}

# graph_data2 = requests.post(api_endpoint2, headers= headers, data= body).json()
graph_data2 = requests.post(api_endpoint2, headers= headers, files= files).json()

# r = requests.post(api_endpoint2, files=files, headers=headers)
print("Graph API call result: %s" % json.dumps(graph_data2, indent=2))