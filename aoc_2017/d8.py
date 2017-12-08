from collections import defaultdict

test = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""


def init_registers(input) -> defaultdict:
    out = defaultdict(int)
    for r in input.split('\n'):
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
        print(parts)
        if parts[1] == 'inc':
            regs[parts[0]] += int(parts[2])
        elif parts[1] == 'dec':
            regs[parts[0]] -= int(parts[2])


if __name__ == '__main__':
    test = open('d8.txt', 'r').read()
    regs = init_registers(test)
    tmp = 0
    for r in test.split('\n'):
        parser(r)
        if tmp <= max(regs.values()):
            tmp = max(regs.values())
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