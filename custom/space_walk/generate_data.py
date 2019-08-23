import sys
from random import random


def get_random(range=3):
    r = round(random() * range, 3)
    if r * 1000 % 2 == 0:
        r *= -1
    if r * 1000 % 3 == 0:
        r = 0.000
    return r


def generate_lines(n, min=-3, max=3):
    lines = []
    for _ in range(n):
        r1 = get_random()
        r2 = get_random()
        r3 = get_random()
        lines.append([r1, r2, r3])
    return lines


def output_line(line):
    print(f"{line[0]:>7.3}{line[1]:>7.3}{line[2]:>7.3}")


print(sys.argv[1])
lines = generate_lines(int(sys.argv[1]))
for line in lines:
    output_line(line)
