import json
import urllib.request

url = urllib.request.urlopen('https://tusitiowp/wp-json/wp/v2/users')

for i in json.loads(url.read()):
    user = i['slug']
    print(user)
