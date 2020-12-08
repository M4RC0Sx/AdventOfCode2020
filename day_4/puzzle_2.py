# Advent of Code 2020 - M4RC0Sx
import re

HGT_REGEX = re.compile('^(1(([5-8][0-9])|(9[0-3]))cm)|((59|6[0-9]|7[0-6])in)$')
HCL_REGEX = re.compile('^#([0-9]|[a-f]){6}$')
ECL_REGEX = re.compile('^(amb|blu|brn|gry|grn|hzl|oth)$')
PID_REGEX = re.compile('^\d{9}$')


with open('input.dat', 'r') as f:
    rows = f.readlines()

rows.extend(('\n', '\n'))

valid_passports = 0

passport = {}
for r in rows:

    if r == '\n':
        if (len(passport) == 8) or (len(passport) == 7 and 'cid' not in passport):
            if int(passport['byr']) not in range(1920, 2002+1) or \
               int(passport['iyr']) not in range(2010, 2020+1) or \
               int(passport['eyr']) not in range(2020, 2030+1) or \
               HGT_REGEX.match(passport['hgt']) is None or \
               HCL_REGEX.match(passport['hcl']) is None or \
               ECL_REGEX.match(passport['ecl']) is None or \
               PID_REGEX.match(passport['pid']) is None:

                passport = {}
                continue

            print(passport)
            valid_passports += 1
        passport = {}

    else:
        for s in r.split(' '):
            passport[s.split(':')[0].strip()] = s.split(':')[1].strip()

print(valid_passports)
exit()
