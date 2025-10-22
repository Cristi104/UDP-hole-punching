from time import sleep

import requests

sleep(10)
res = requests.get('http://10.42.0.2:80')
print(res.json())