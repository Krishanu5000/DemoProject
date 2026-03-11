from itertools import chain
import re

f = open('C:/Users/krish/IdeaProjects/DemoProject/Data/sample3.txt', 'r')
# print(f.read())

s = f.read()
print(s)

l = [i.split(" ") for i in s.splitlines()]
l = list(chain(*l))

d = {}

for i in l:
    k = re.sub(r'[^a-zA-Z0-9]', '', i.strip())
    if k not in d.keys():
        d[k] = 1
    else:
        d[k] += 1
print(d)
