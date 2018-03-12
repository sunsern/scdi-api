import requests
import uuid
from time import sleep
import random
from datetime import datetime, timedelta

BASE_URL = 'https://scdi-api.philinelabs.net'
AUTH_URL = BASE_URL + '/auth/basic/api_key'
API_URL = BASE_URL + '/api/v1/'

DEFAULT_USERNAME = 'admin'
APIKEY = ''

BUCKET = 'gps_demo'
BUCKET_SCHEMA = {
    "type": "geotemporal",
    "columns" : [
            {
                "name": "ts",
                "type": "timestamp",
                "indexed": True
            },
            {
                "name": "lat",
                "type": "double",
                "indexed": True
            },
            {
                "name": "lng",
                "type": "double",
                "indexed": True
            },
            {
                "name": "imei",
                "type": "varchar",
                "indexed": False
            }
        ]
}


def getApiKey(username, password):
    r = requests.get(AUTH_URL, auth=(username, password))
    return r.json()['apiKey']

def createBucket(username, bucketname, payload):
    headers = { 'APIKEY' : APIKEY }
    r = requests.post(API_URL + username + '/' + bucketname + '?create',
        headers=headers, json=payload)
    return r

def dropBucket(username, bucketname):
    headers = { 'APIKEY' : APIKEY }
    r = requests.delete(API_URL + username + '/' + bucketname + '?delete',
        headers=headers)
    return r

def getBucket(username, bucketname):
    headers = { 'APIKEY' : APIKEY }
    r = requests.get(API_URL + username + '/' + bucketname + '?meta',
        headers=headers)
    return r

def sendData(username, bucketname, json):
    headers = { 'APIKEY' : APIKEY }
    uri = API_URL + username + '/' + bucketname
    r = requests.put(uri, headers=headers, json=json)
    return r

def query(username, bucketname):
    headers = { 'APIKEY' : APIKEY }
    tminus10 = datetime.now() - timedelta(seconds=10)
    uri = API_URL + username + '/' + bucketname
    r = requests.post(uri + '?query', headers=headers, json={
	       "fromEpoch": tminus10.strftime('%s')
        })
    return r


print "Start simulation"

base_lat = 13.7927155
base_lng = 100.3237294

while True:
    lat = base_lat + (random.random() - 0.5) * 0.04
    lng = base_lng + (random.random() - 0.5) * 0.04
    imei = uuid.uuid4().hex
    current = datetime.now().strftime('%s')
    data = {
        'ts': current,
        'lat': lat,
        'lng': lng,
        'imei': imei
    }
    print "sending..",data,
    print sendData(DEFAULT_USERNAME, BUCKET, data).status_code
    sleep(0.2)
