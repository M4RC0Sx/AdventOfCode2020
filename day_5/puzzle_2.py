# Advent of Code 2020 - M4RC0Sx

MIN_ROW = 0
MAX_ROW = 127

MIN_COL = 0
MAX_COL = 7


with open('input.dat', 'r') as f:
    rows = f.readlines()

rows.extend(('\n', '\n'))

seat_ids = []

for r in rows:

    row_interval = (MIN_ROW, MAX_ROW)
    col_interval = (MIN_COL, MAX_COL)

    for fb in r[0:7]:
        if fb == 'F':
            row_interval = (row_interval[0], int(
                (row_interval[0]+row_interval[1]+1)/2)-1)
        if fb == 'B':
            row_interval = (
                int((row_interval[0]+row_interval[1]+1)/2), row_interval[1])

    row = min(row_interval)
    # print(row)

    for lr in r[7:]:
        if lr == 'L':
            col_interval = (col_interval[0], int(
                (col_interval[0]+col_interval[1]+1)/2)-1)
        if lr == 'R':
            col_interval = (
                int((col_interval[0]+col_interval[1]+1)/2), col_interval[1])

    col = max(col_interval)
    # print(col)

    seat_id = row*8 + col
    seat_ids.append(seat_id)

for my_seat in range(min(seat_ids), max(seat_ids)+1):

    if my_seat not in seat_ids and my_seat-1 in seat_ids and my_seat+1 in seat_ids:
        print(my_seat)

exit()
