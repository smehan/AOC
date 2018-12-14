from functools import reduce
from itertools import zip_longest as zipl, product as p, accumulate
from operator import xor


def reverse_sublist(l, a, b):
    if a <= b: l[a:b] = l[a:b][::-1]
    else: r = (l[a:]+l[:b])[::-1]; l[a:], l[:b] = r[:len(l)-a], r[-b or len(r):]
    return l


def hash_round(lens, elems, pos=0, skip=0, accumulator=lambda x, y: (y[0], reduce(sum, x))):
    for (skip, s), pos in accumulate(zipl(enumerate(lens, skip), [pos]), accumulator):
        reverse_sublist(elems, pos % len(elems), (pos+s) % len(elems))
    return elems, skip+s+pos, skip+1


def knothash_list(input, n=256, g=16, rounds=64, suffix=[17, 31, 73, 47, 23], pos=0, skip=0):
    elems, lengths = [*range(n)], [ord(c) for c in input.strip()] + suffix
    for _ in range(rounds): elems, pos, skip = hash_round(lengths, elems, pos, skip)
    return [reduce(xor, elems[g*k:g*(k+1)]) for k in range(n//g)]


def make_matrix(k, n=128, kh=knothash_list, r=range):
    return [[b for h in kh(f'{k}-{i}') for b in map(int, f'{h:08b}')] for i in r(n)]


def solve1(matrix): return sum(r.count(1) for r in matrix)


def solve2(m, N=0, r={*range(128)}):
    for N, q in ((N+1, [S]) for S in p(*[r]*2) if m[S[0]][S[1]]):
        while q: x, y = q.pop(); m[x][y] = 0; q.extend(
                 n for n in ((x+1, y), (x-1, y), (x, y+1), (x, y-1))
                 if {*n} < r and m[n[0]][n[1]])
    return N


m = make_matrix('stpzcrnm')
part1, part2 = solve1(m), solve2(m)
print(part1, part2)


