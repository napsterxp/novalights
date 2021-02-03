import requests
from time import sleep
url = "http://192.168.0.56/api/9cZcjXWstjsDlmoBryvToRh-uLiO3dzety5oEFyE/groups/0/action"
def red():
    payload = "{\r\n\"on\" : \"tru\",\r\n             \"bri\": 254,\r\n            \"hue\": 65267,\r\n            \"sat\": 254,\r\n            \"transitiontime\": 0\r\n            }"
    headers = {
    'Content-Type': 'text/plain'
    }
    response = requests.request("PUT", url, headers=headers, data = payload)
def blue():
    payload = "{\r\n\"on\" : \"tru\",\r\n       \"bri\": 254,\r\n\r\n            \"hue\": 42496,\r\n            \"sat\": 243\r\n            }"
    headers = {
    'Content-Type': 'text/plain'
    }
    response = requests.request("PUT", url, headers=headers, data = payload)
def white():
    payload = "{\r\n\t\"on\" : true,\r\n    \"bri\": 254,\r\n    \"hue\": 34816,\r\n    \"sat\": 3,\r\n    \"ct\": 209,\r\n    \"colormode\": \"ct\"\r\n    }"
    headers = {
    'Content-Type': 'text/plain'
    }
    response = requests.request("PUT", url, headers=headers, data = payload)
def yellow():
    payload = "{\r\n\"on\" : \"tru\",\r\n       \"bri\": 254,\r\n\r\n            \"hue\": 7936,\r\n            \"sat\": 254\r\n            }"
    headers = {
    'Content-Type': 'text/plain'
    }
    response = requests.request("PUT", url, headers=headers, data = payload)
def green():
    payload = "{\r\n\"on\" : \"tru\",\r\n             \"bri\": 254,\r\n            \"hue\": 18432,\r\n            \"sat\": 254,\r\n            \"transitiontime\": 0\r\n            }"
    headers = {
    'Content-Type': 'text/plain'
    }
    response = requests.request("PUT", url, headers=headers, data = payload)
def dbo():
    payload = "{\r\n\t\"on\" : false\r\n            }"
    headers = {
    'Content-Type': 'text/plain'
    }
    response = requests.request("PUT", url, headers=headers, data = payload)

def redflash():
    red()
    sleep(0.5)
    dbo()
    sleep(1.5)
    red()
    sleep(0.5)
    dbo()
    sleep(1.5)
    red()
    sleep(0.5)
    dbo()
    sleep(1.5)
    red()
    sleep(0.5)
    dbo()
    sleep(1.5)
    red()
    sleep(0.5)
    dbo()
    sleep(1.5)


def greenflash():
    green()
    sleep(0.5)
    dbo()
    sleep(1.5)
    green()
    sleep(0.5)
    dbo()
    sleep(1.5)
    green()
    sleep(0.5)
    dbo()
    sleep(1.5)
    green()
    sleep(0.5)
    dbo()
    sleep(1.5)
    green()
    sleep(0.5)
    dbo()
    sleep(1.5)

