# Advent of Code 2020 - M4RC0Sx

with open('input.dat', 'r') as f:
    rows = f.readlines()

buffer = {}
for r in rows:

    num = int(r)
    diff = 2020 - num

    try:
        if(buffer[diff]):
            print(num*diff)
            exit()
    except KeyError:
        pass

    buffer[num] = True
