import requests
url = "http://192.168.0.56/api/fd4wFBBUmcFe9AdcPS7Waw72TUSViISK4oXRs96q/groups/0/action"
def red():
    payload = "{\r\n\"on\" : true,\r\n             \"bri\": 254,\r\n            \"hue\": 65267,\r\n            \"sat\": 254,\r\n            \"transitiontime\": 0\r\n            }"
    headers = {
    'Content-Type': 'text/plain'
    }
    response = requests.request("PUT", url, headers=headers, data = payload)
def blue():
    payload = "{\r\n\"on\" : true,\r\n        \"bri\": 254,\r\n\r\n            \"hue\": 46596,\r\n            \"sat\": 251\r\n            }"
    headers = {
    'Content-Type': 'text/plain'
    }
    response = requests.request("PUT", url, headers=headers, data = payload)
def white():
    payload = "{\r\n\"on\" : true,\r\n        \"bri\": 254,\r\n\r\n            \"hue\": 34412,\r\n            \"sat\": 254\r\n            }"
    headers = {
    'Content-Type': 'text/plain'
    }
    response = requests.request("PUT", url, headers=headers, data = payload)
def redflash():
    payload = "{\r\n\"on\" : true,\r\n   \"bri\": 254,\r\n             \"hue\": 65267,\r\n           \"sat\": 254,\r\n         \"alert\": \"lselect\"\r\n            }"
    headers = {
    'Content-Type': 'text/plain'
    }
    response = requests.request("PUT", url, headers=headers, data = payload)
def yellow():
    payload = "{\r\n\"on\" : true,\r\n       \"bri\": 254,\r\n\r\n            \"hue\": 13133,\r\n            \"sat\": 252\r\n            }"
    headers = {
    'Content-Type': 'text/plain'
    }
    response = requests.request("PUT", url, headers=headers, data = payload)
def greenflash():
    payload = "{\r\n\"on\" : true,\r\n   \"bri\": 254,\r\n             \"hue\": 25653,\r\n           \"sat\": 254,\r\n         \"alert\": \"lselect\"\r\n            }"
    headers = {
    'Content-Type': 'text/plain'
    }
    response = requests.request("PUT", url, headers=headers, data = payload)
def off():
    payload = "{\r\n\"on\" : false\r\n            }"
    headers = {
    'Content-Type': 'text/plain'
    }
    response = requests.request("PUT", url, headers=headers, data = payload)
