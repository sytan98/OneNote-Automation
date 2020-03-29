import json
import logging
import yaml
import requests
import msal
import codecs
import pprint
import codecs
from requests_toolbelt import MultipartEncoder
from datetime import datetime



def onenote(api_endpoint, settings, token):
    headers={'Authorization': 'Bearer ' + token['access_token'], "content-type": "text/html"}

    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")

    body = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>{}</title>
            <meta name="created" content="{}" />
        </head>
        <body>
            <p>Lecture</p>
            <img data-render-src="name:fileBlock1" />
            <object data-attachment="lecture15(1).pdf" data="name:fileBlock1" type="application/pdf" />
        </body>
        </html>
        '''.format("Test", dateTimeObj)

    fin = open('OnlineEnrolment_01701371.pdf', 'rb')
    # files = {'name': (<filename>, <file object>, <content type>, <per-part headers>)}
    files = {'presentation': (None, body, 'text/html'),
            'fileBlock1': (None, fin, 'application/pdf')}


    headers={'Authorization': 'Bearer ' + token['access_token']}

    # graph_data2 = requests.post(api_endpoint2, headers= headers, data= body).json()
    graph_data2 = requests.post(api_endpoint, headers= headers, files= files).json()

    # r = requests.post(api_endpoint2, files=files, headers=headers)
    pprint.pprint(json.dumps(graph_data2, indent=2))