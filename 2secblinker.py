import requests
puturl = "http://192.168.0.54/api/fd4wFBBUmcFe9AdcPS7Waw72TUSViISK4oXRs96q/groups/0/action"
def flashred():
    payload = "{\"on\": true,\r\n            \"bri\": 254,\r\n            \"hue\": 65267,\r\n            \"sat\": 253,\r\n            \"alert\": \"none\",\r\n            \"transitiontime\": 0\r\n            }"
    headers = {
    'Content-Type': 'text/plain'
    }
    response = requests.request("PUT", puturl, headers=headers, data = payload)
def flashblue():
    payload = "          {  \"on\": true,\r\n            \"bri\": 254,\r\n            \"hue\": 46596,\r\n            \"sat\": 251,\r\n            \"transitiontime\": 0\r\n            }"
    headers = {
    'Content-Type': 'text/plain'
    }
    response = requests.request("PUT", puturl, headers=headers, data = payload)
from time import sleep

try:
    while True:
        flashred()
        sleep(2)
        flashblue()
        sleep(2)

finally:
    print ("got to the end now")
