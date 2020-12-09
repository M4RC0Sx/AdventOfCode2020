# Advent of Code 2020 - M4RC0Sx

with open('input.dat', 'r') as f:
    rows = f.readlines()

rows.extend(('\n', '\n'))

total_answers = 0

buffer = {}
for r in rows:

    if r == '\n':

        total_answers += len(buffer)
        buffer = {}
    else:
        for letter in r.strip():
            buffer[letter] = True


print(total_answers)
exit()
