# Advent of Code 2020 - M4RC0Sx

with open('input.dat', 'r') as f:
    rows = f.readlines()

trees = 0
x_pos = 0
row_len = len(rows[0].strip())

for i in range(0, len(rows)):

    if rows[i][x_pos % row_len] == '#':
        trees += 1

    x_pos += 3


print(trees)
exit()
