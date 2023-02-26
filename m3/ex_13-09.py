import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_1710705.json'

link = urllib.request.urlopen(url)
data = link.read().decode()

js = json.loads(data)

counts = 0
for i in js['comments']:
    counts += i['count']

print('Count:', counts)
