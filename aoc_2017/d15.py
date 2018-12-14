"""
Generator A starts with 783
Generator B starts with 325
"""

from itertools import islice as i, accumulate as a, repeat as r, filterfalse as f

m, G = 65535, lambda s, m, d=2**31-1: a(r(s*m%d), lambda v, _: v*m%d)
s, P = sum, {(65, 16807): lambda x: x&3, (8921, 48271): lambda x: x&7}
M = lambda g, n: s(len({v&m for v in V}) < 2 for V in i(zip(*g), n+1))
M((G(*p) for p in P), 4*10**7), M((f(P[p], G(*p)) for p in P), 5*10**6)

import itertools

def gen(val, mult, check=None):
    while True:
        val = (val * mult) % 2147483647
        if check is None or val % check == 0:
            yield val


init1, init2 = [783, 325]

gen1, gen2 = gen(init1, 16807), gen(init2, 48271)

part1 = 0

for a, b in itertools.islice(zip(gen1, gen2), 40000000):
    if a % 65536 == b % 65536:
        part1 += 1

print('Part 1:', part1)

gen1, gen2 = gen(init1, 16807, 4), gen(init2, 48271, 8)

part2 = 0

for a, b in itertools.islice(zip(gen1, gen2), 5000000):
    if a % 65536 == b % 65536:
        part2 += 1

print('Part 1:', part2)

# another


def solve(ga, gb, iterations, needs_multiple):
    count = 0
    for i in range(iterations):
        while True:
            ga *= 16807
            ga %= 2147483647
            if not needs_multiple or ga % 4 == 0:
                break
        while True:
            gb *= 48271
            gb %= 2147483647
            if not needs_multiple or gb % 8 == 0:
                break
        if (ga & 65535 == gb & 65535):
            count += 1
    return count

print(solve(init1, init2, 40_000_000, False))
print(solve(init1, init2, 5_000_000, True))