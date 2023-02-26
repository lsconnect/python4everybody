# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail
# messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the
# mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
# they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum
# loop to find the most prolific committer.

filename = "mbox-short.txt"
document = open(filename)

counts = dict()

for line in document:
    line = line.rstrip()
    if line.startswith("From"):
        words = line.split()
        if len(words) > 2:
            names = words[1]

            counts[names] = counts.get(names, 0) + 1

sender = None
count = None
for keys, values in counts.items():
    if sender is None or count is None:
        sender = keys
        count = values
    elif values > count:
        sender = keys
        count = values

print(sender, count)
