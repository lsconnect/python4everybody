import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('15-08/dbmusic.sqlite')
cur = conn.cursor()

# Clear table data
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

file = open("15-08/Library.xml")


def search(d, key):
    success = False
    for child in d:
        if success:
            return child.text
        if child.tag == 'key' and child.text == key:
            success = True
    return None


convert = ET.parse(file)
all = convert.findall('dict/dict/dict')
print('Count:', len(all))
for each in all:
    if search(each, 'Track ID') is None:
        continue

    name = search(each, 'Name')
    artist = search(each, 'Artist')
    album = search(each, 'Album')
    genre = search(each, 'Genre')
    count = search(each, 'Play Count')
    rating = search(each, 'Rating')
    length = search(each, 'Total Time')

    if name is None or artist is None or album is None or genre is None:
        continue

    print(name, artist, album, genre, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES (?)''', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''',
                (name, album_id, genre_id, length, rating, count))

    conn.commit()
