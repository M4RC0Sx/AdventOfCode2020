# Advent of Code 2020 - M4RC0Sx

with open('input.dat', 'r') as f:
    rows = f.readlines()

size = len(rows)
for i in range(0, size-2):
    for j in range(i+1, size-1):
        for k in range(j+1, size):
            if int(rows[i]) + int(rows[j]) + int(rows[k]) == 2020:
                print(int(rows[i]) * int(rows[j]) * int(rows[k]))
                exit()
