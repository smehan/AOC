from collections import deque
seq = list(range(0, 5))
lengths = deque([3, 4, 1, 5])
skip_size = 0

pos = 0
while lengths:
    current_l = lengths.popleft()
    sub = seq[pos:pos + current_l]
    print(current_l, sub, pos)
    pos = (pos + current_l + skip_size) % len(seq)
    skip_size += 1

"""
Suppose we instead only had a circular list containing five elements, 0, 1, 2, 3, 4, and were given input lengths of 3, 4, 1, 5.

The list begins as [0] 1 2 3 4 (where square brackets indicate the current position).
The first length, 3, selects ([0] 1 2) 3 4 (where parentheses indicate the sublist to be reversed).
After reversing that section (0 1 2 into 2 1 0), we get ([2] 1 0) 3 4.
Then, the current position moves forward by the length, 3, plus the skip size, 0: 2 1 0 [3] 4. Finally, the skip size increases to 1.
The second length, 4, selects a section which wraps: 2 1) 0 ([3] 4.
The sublist 3 4 2 1 is reversed to form 1 2 4 3: 4 3) 0 ([1] 2.
The current position moves forward by the length plus the skip size, a total of 5, causing it not to move because it wraps around: 4 3 0 [1] 2. The skip size increases to 2.
The third length, 1, selects a sublist of a single element, and so reversing it has no effect.
The current position moves forward by the length (1) plus the skip size (2): 4 [3] 0 1 2. The skip size increases to 3.
The fourth length, 5, selects every element starting with the second: 4) ([3] 0 1 2. Reversing this sublist (3 0 1 2 4 into 4 2 1 0 3) produces: 3) ([4] 2 1 0.
Finally, the current position moves forward by 8: 3 4 2 1 [0]. The skip size increases to 4.
"""

from functools import reduce
from itertools import accumulate, zip_longest as zipl
from operator import mul, xor

def reverse_sublist(l, a, b):
    if a <= b: l[a:b] = l[a:b][::-1]
    else: r = (l[a:]+l[:b])[::-1]; l[a:], l[:b] = r[:len(l)-a], r[-b or len(r):]

def hash_round(lens, elems, pos=0, skip=0, accumulator=lambda x, y: (y[0], reduce(sum, x))):
    for (skip, s), pos in accumulate(zipl(enumerate(lens, skip), [pos]), accumulator):
        reverse_sublist(elems, pos % len(elems), (pos+s) % len(elems))
    return elems, skip+s+pos, skip+1

def solve1(input, n=256):
    return mul(*hash_round([int(l) for l in input.split(',')], list(range(n)))[0][:2])

def solve2(input, n=256, g=16, rounds=64, suffix=[17, 31, 73, 47, 23], pos=0, skip=0):
    elems, lengths = [*range(n)], [ord(c) for c in input.strip()] + suffix
    for _ in range(rounds): elems, pos, skip = hash_round(lengths, elems, pos, skip)
    return bytes(reduce(xor, elems[g*k:g*(k+1)]) for k in range(n//g)).hex()

print(solve1(open('d10.txt', 'r').read()))
print(solve2(open('d10.txt', 'r').read()))