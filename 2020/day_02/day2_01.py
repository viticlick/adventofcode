import re

f = open('input.txt','r')
counter = 0
for line in f.readlines():
    (a,b,c,d) = re.findall('(\d+)-(\d+) (\w): (\w+)', line)[0]
    if int(a) <= len(re.findall(c,d)) <= int(b):
        counter = counter + 1
print(counter)
