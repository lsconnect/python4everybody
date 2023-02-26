import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_1710704.xml'
xml = urllib.request.urlopen(url).read()

print(xml)

tree = ET.fromstring(xml)
counts = tree.findall('comments/comment')
print('Count:', len(counts))

s = 0
for x in counts:
    s += int(x.find('count').text)

print('Sum:', s)
