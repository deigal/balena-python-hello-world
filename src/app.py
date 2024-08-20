import requests
import random
import datetime
import time


x = range (100)
url = 'https://api.powerbi.com/beta/f5622c43-8e64-4863-aed4-0cc4908d3c88/datasets/0c21a444-f22c-4e52-831a-23c3374c8da6/rows?experience=power-bi&key=7gjVKD%2F5nm%2BxHV3ynzgitKEIyCJUIOrXT9BYGSp86uCgGViU0MFqexQ3J2RU4GXtdvQW9wmcxAjbUdPqwixqDA%3D%3D'

temp = 30

for n in x:
    y = random.uniform(-1, 1)
    temp = temp + y
    ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    myobj = [
    {
    "Temperature" :temp,
    "Timestamp" :ts
    }
    ]
    r = requests.post(url, json = myobj)
    time.sleep(1)
    print(myobj)
    print(r.status_code)
