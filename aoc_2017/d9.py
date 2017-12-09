from collections import defaultdict
import time
import sys

class Solver(object):

    def __init__(self):
        self.groups = 0
        self.records = defaultdict(int)
        self.lex = {'{': self.br, '}': self.brc, '<': self.gar, '>': self.garc, '!': self.bang}


    def br(self):
        if not self.records['gar']:
            self.records['br'] += 1

    def brc(self):
        if not self.records['gar']:
            self.records['br'] -= 1
            self.groups += 1

    def gar(self):
        if not self.records['gar']:
            self.records['gar'] += 1

    def garc(self):
        self.records['gar'] -= 1

    def bang(self):
        if self.records['gar']:
            self.records['bang'] += 1

    def parser(self, c):
        print(f'\r{c} - {self.records} - {self.groups}')
        time.sleep(0.001)
        sys.stdout.flush()
        if c in self.lex.keys():
            self.lex[c]()


def process():
    soln = Solver()
    with open('d9.txt') as f:
        while True:
            if soln.records['bang']:
                _ = f.read(1)
                soln.records['bang'] -= 1
            c = f.read(1)
            if not c:
                print(f"Groups: {soln.groups}")
                break
            soln.parser(c)


def debug_process(s):
    soln = Solver()
    for i in range(len(s)):
        if soln.records['bang']:
            soln.records['bang'] -= 1
            continue
        soln.parser(s[i])
    print(f'{s}')
    print(f"Groups: {soln.groups}")


# process()
test = ['<>', '<random chars>', '{}', '{{{}}}', '<<<<>', '<{!>}>', '<!!>', '<!!!>>', '<{o"i!a,<{i<a>', '{{},{}}',
        '{{{},{},{{}}}}', '{<{},{},{{}}>}', '{<a>,<a>,<a>,<a>}', '{{<a>},{<a>},{<a>},{<a>}}', '{{<!>},{<!>},{<!>},{<a>}}']

# for t in test:
#     debug_process(t)
debug_process(open('d9.txt', 'r').read())
"""
Here are some self-contained pieces of garbage:

<>, empty garbage.
<random characters>, garbage containing random characters.
<<<<>, because the extra < are ignored.
<{!>}>, because the first > is canceled.
<!!>, because the second ! is canceled, allowing the > to terminate the garbage.
<!!!>>, because the second ! and the first > are canceled.
<{o"i!a,<{i<a>, which ends at the first >.
Here are some examples of whole streams and the number of groups they contain:

{}, 1 group.
{{{}}}, 3 groups.
{{},{}}, also 3 groups.
{{{},{},{{}}}}, 6 groups.
{<{},{},{{}}>}, 1 group (which itself contains garbage).
{<a>,<a>,<a>,<a>}, 1 group.
{{<a>},{<a>},{<a>},{<a>}}, 5 groups.
{{<!>},{<!>},{<!>},{<a>}}, 2 groups (since all but the last > are canceled).
Your goal is to find the total score for all groups in your input. Each group is assigned a score which is one more than the score of the group that immediately contains it. (The outermost group gets a score of 1.)

{}, score of 1.
{{{}}}, score of 1 + 2 + 3 = 6.
{{},{}}, score of 1 + 2 + 2 = 5.
{{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
{<a>,<a>,<a>,<a>}, score of 1.
{{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.
"""