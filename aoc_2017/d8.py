from collections import defaultdict
import operator as op

test = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

compartors = {'>': op.gt, '>=': op.ge, '<': op.lt, '<=': op.le, '==': op.eq, '!=': op.ne}


def init_registers(input) -> defaultdict:
    out = defaultdict(int)
    for r in input.splitlines():
        out[r.split(' ')[0]]
    return out


def cond(args) -> bool:
    if args[1] == '>' and (regs[args[0]] > int(args[2])):
        return True
    elif args[1] == '>=' and (regs[args[0]] >= int(args[2])):
        return True
    elif args[1] == '<' and (regs[args[0]] < int(args[2])):
        return True
    elif args[1] == '<=' and (regs[args[0]] <= int(args[2])):
        return True
    elif args[1] == '==' and (regs[args[0]] == int(args[2])):
        return True
    elif args[1] == '!=' and (regs[args[0]] != int(args[2])):
        return True
    return False


def parser(s: str):
    parts = s.split(' ')
    if parts[3] == 'if' and cond(parts[4:7]):
        regs[parts[0]] += (1 if parts[1] == 'inc' else -1) * int(parts[2])


if __name__ == '__main__':
    test = open('d8.txt', 'r').read()
    regs = init_registers(test)
    tmp = float('-inf')
    for r in test.splitlines():
        parser(r)
        tmp = max(tmp, max(regs.values()))
    print(max(sorted(regs.values())), tmp)





"""b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
These instructions would be processed as follows:

Because a starts at 0, it is not greater than 1, and so b is not modified.
a is increased by 1 (to 1) because b is less than 5 (it is 0).
c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
c is increased by -20 (to -10) because c is equal to 10.
After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU 
doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine."""

"""
import operator as op
from collections import defaultdict
comps = {'>': op.gt, '<': op.lt, '>=': op.ge, '<=': op.le, '!=': op.ne, '==': op.eq}

def solve(input, mx=float('-inf'), ops=dict(inc=1, dec=-1)):
    regs = defaultdict(int)
    for r1, op, v1, _, r2, c, v2 in [l.split() for l in input.splitlines() if l]:
        regs[r1] += ops.get(op) * int(v1) if comps[c](regs[r2], int(v2)) else 0
        mx = max(mx, regs[r1])
    return max(regs.values()), mx

part1, part2 = solve(input)
"""