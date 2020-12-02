import re
from operator import xor

f = open('input.txt','r')
counter = 0
for line in f.readlines():
    (a,b,c,d) = re.findall('(\d+)-(\d+) (\w): (\w+)', line)[0]
    first_occurence = d[int(a) - 1] == c
    last_occurence = d[int(b) - 1] == c
    if xor(first_occurence, last_occurence):
        counter = counter + 1
print(counter)
