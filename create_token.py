#!/usr/bin/python
# ~*~ coding: utf-8 ~*~


LOGIN = 'jelastic@login'
PASSWORD = 'password'
TOKEN_DESCRIPTION = 'gitlab'

# defaults for mycloud.by
APPID = '58bdf83fea6af021e0c94ba13730fd6b'
JDOMAIN = 'mycloud.by'

import requests, json, sys

URL = 'https://app.' + JDOMAIN + '/1.0/users/authentication/rest/signin'

HEADERS = {
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, sdch',
	'Accept-Language': 'en,en-US;q=0.8,ru;q=0.6,uk;q=0.4',
	'Connection': 'keep-alive'
}

DATA1 = {
	'login':LOGIN,
	'password':PASSWORD
}

response = requests.post(URL, headers=HEADERS, data=DATA1)
response.content
data=json.loads(json.dumps(response.json()))

# to get all available permissions
#URL2 = 'https://app.' + JDOMAIN + '/1.0/users/authentication/rest/gettokenapilist'
URL2 = 'https://app.' + JDOMAIN + '/1.0/users/authentication/rest/createtoken'
DATA2 = {
	'session': str(data['session']),
	'apiList': ['environment.control.RedeployContainerById', 'environment.control.RedeployContainersByGroup'],
	'description': TOKEN_DESCRIPTION
}

response2 = requests.post(URL2, headers=HEADERS, data=DATA2)
response2.content
data2=json.loads(json.dumps(response2.json()))

print data2
