
from time import sleep
import datetime

count = 0

while True:
    now = datetime.datetime.now()
    second = now.second
    count = count +1
    if count < 150:
        print(count)
    else:
        count = 0
    sleep(0.5)
    #print(count)
