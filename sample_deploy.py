#!/usr/bin/python
# ~*~ coding: utf-8 ~*~

APPID = '58bdf83fea6af021e0c94ba13730fd6b'
TOKEN = 'get token by create_token.py'

ENV = 'myenvname'
STAGING_ID = 10000

JDOMAIN = 'mycloud.by'

import requests, json, sys

if len (sys.argv) != 2 :
    print "Usage: " + sys.argv[0] + " [staging|production]"
    sys.exit(1)

mode = sys.argv[1]

if mode == 'staging':
	URL = 'https://app.' + JDOMAIN + '/1.0/environment/control/rest/redeploycontainerbyid'
	DATA = {
		'token': TOKEN,
		'envName': ENV,
		'nodeId': STAGING_ID,
		'tag': 'master',
		'useExistingVolumes': True
	}
if mode == 'production':
	URL = 'https://app.' + JDOMAIN + '/1.0/environment/control/rest/redeploycontainersbygroup'
	DATA = {
		'token': TOKEN,
		'envName': ENV,
		'nodeGroup': 'cp',
		'tag': 'latest',
		'useExistingVolumes': True
	}

if not DATA:
	sys.exit(1)

response = requests.post(URL, headers=HEADERS, data=DATA)
response.content
data=json.loads(json.dumps(response.json()))

#print r.json()
print data
