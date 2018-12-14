from collections import Counter as C
ds = ['sw', 's', 'se', 'ne', 'n', 'nw']
w = {d: [ds[(i+k)%6] for k in [3, 0, -1, 1]] for i, d in enumerate(ds)}


def solve(input, f=0, s=None, u=lambda s, d, k: k in s and {k: -1} or {d: 1}):
    for d in input.strip().split(','):
        s = s or C();
        f = max(f, sum(s.values()));
        s += u(s, d, w[d][0])
        for b, a, c in (v[1:] for v in w.values() if {*v[2:]} <= {*+s}):
            m = min(s[a], s[c]); s -= {a: m, b: -m, c: m}
    d = sum(s.values()); return d, max(f, d)

print(solve(open('d11.txt', 'r').read()))