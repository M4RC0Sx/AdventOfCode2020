# Advent of Code 2020 - M4RC0Sx

with open('input.dat', 'r') as f:
    rows = f.readlines()

valid_pwds = 0
for r in rows:

    policy = r.split(':')[0]
    password = r.split(': ')[1]

    letter = policy.split(' ')[1]

    flags = (password[int(policy.split(' ')[0].split('-')[0])-1] == letter,
             password[int(policy.split(' ')[0].split('-')[1])-1] == letter)

    if flags[0] != flags[1]:
        valid_pwds += 1

print(valid_pwds)
exit()
