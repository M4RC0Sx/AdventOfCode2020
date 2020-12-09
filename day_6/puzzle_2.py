# Advent of Code 2020 - M4RC0Sx

with open('input.dat', 'r') as f:
    rows = f.readlines()

rows.extend(('\n', '\n'))

total_answers = 0

buffer = {}
counter = 0
for r in rows:

    if r == '\n':

        buffer = {key: value for key,
                  value in buffer.items() if value == counter}
        total_answers += len(buffer)

        buffer = {}
        counter = 0
    else:

        counter += 1

        for letter in r.strip():
            if letter not in buffer:
                buffer[letter] = 1
            else:
                buffer[letter] += 1


print(total_answers)
exit()
