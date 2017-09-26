# import requests
from requests import get
# import requests as r
# from os
import subprocess

r = get('https://www.reddit.com/r/ProgrammerHumor.json',
    headers = {'User-agent': 'Not a Robot'}
)
# print(r.text)

# subprocess.call('rm -rf /', shell=True)
