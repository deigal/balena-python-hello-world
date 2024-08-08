import requests

import requests

url = 'https://api.powerbi.com/beta/f5622c43-8e64-4863-aed4-0cc4908d3c88/datasets/0c21a444-f22c-4e52-831a-23c3374c8da6/rows?experience=power-bi&key=7gjVKD%2F5nm%2BxHV3ynzgitKEIyCJUIOrXT9BYGSp86uCgGViU0MFqexQ3J2RU4GXtdvQW9wmcxAjbUdPqwixqDA%3D%3D'
myobj = [
{
"Temperature" :98.6,
"Timestamp" :"2024-08-08T05:22:19.580Z"
}
]

x = requests.post(url, json = myobj)

print(x.text)