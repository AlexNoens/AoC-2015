import json
import re
pattern= r"-?\d{1,5}"
file = open("Day12/input.txt","r")
raw = file.read()

matches = re.findall(pattern, raw)

total = 0
for each in matches:
    total += int(each)

print(total)
