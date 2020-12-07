# Advent of Code 2020 - M4RC0Sx
methods = (
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
)


with open('input.dat', 'r') as f:
    rows = f.readlines()

row_len = len(rows[0].strip())

result = 1
for method in methods:

    trees = 0
    x_pos = 0
    for i in range(0, len(rows), method[1]):

        if rows[i][x_pos % row_len] == '#':
            trees += 1

        x_pos += method[0]

    print(trees)
    result = result * trees

print(result)
exit()
