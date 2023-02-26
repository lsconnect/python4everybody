import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/known_by_Arturo.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

count = int(input("Count: "))
position = int(input('Position: ')) - 1

links = soup('a')
while count > 0:
    url = links[position].get('href', None)
    name = links[position].contents[0]
    print(name)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    links = soup('a')
    count -= 1
