import re

file = "regex_sum_1710700.txt"
handler = open(file)

s = 0

for line in handler:
    line = line.rstrip()
    result = re.findall("[0-9]+", line)
    for n in result:
        s += + int(n)

print(s)
