# Advent of Code 2020 - M4RC0Sx

with open('input.dat', 'r') as f:
    rows = f.readlines()

rows.extend(('\n', '\n'))

valid_passports = 0

passport = {}
for r in rows:

    if r == '\n':
        if len(passport) == 8:
            valid_passports += 1
        elif len(passport) == 7 and 'cid' not in passport:
            valid_passports += 1

        passport = {}

    else:
        for s in r.split(' '):
            passport[s.split(':')[0].strip()] = s.split(':')[1].strip()

print(valid_passports)
exit()
