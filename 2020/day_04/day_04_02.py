#! /usr/bin/env  python3
import re, sys

def find_values(text):
    return set(re.findall(r"""
            \b(
            byr:(19[2-9][0-9]|200[0-2])\b
            |iyr:(20(1[0-9]|20))\b
            |eyr:(20(2[0-9]|30))\b
            |hgt:(1([5-8][0-9]|9[0-3])cm)|((59|6[0-9]|7[0-6])in)\b
            |hcl:\#[0-9a-f]{6}\b
            |ecl:(amb|blu|brn|gry|grn|hzl|oth)\b
            |pid:\d{9}\b
            )
            """, text, flags=re.X))

if __name__ == '__main__':
    counter = 0
    with open(sys.argv[1], 'r') as f:
        for entry in re.split(r'(\r\n?|\n){2}', f.read(), flags=re.MULTILINE):
            values = find_values(entry) 
            if len(values) >= 7:
                counter = counter + 1

    print('number of valid entries: ', counter)
