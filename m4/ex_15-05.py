import re
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Clear table data
cur.execute('DELETE FROM Counts')

file = open("mbox.txt")

for line in file:
    if not line.startswith('From: '):  # Ignore
        continue
    line = line.rstrip().split()
    org = re.findall("@(\S+)", line[1])[0]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
