###########################################################
# Copyright (C) 2015-2016 Shawn Mehan <shawn dot mehan at shawnmehan dot com>
# day 10 alternative, more OO in structure for AOC_2016
###########################################################
#
#  -*- coding: utf-8 -*-

# standard libs
from collections import defaultdict

from functools import reduce

# 3rd party libs
import numpy as np

# application libs


class Bot(object):
    def __init__(self):
        self.values = []
        self.low = None
        self.high = None

    def receive(self, value):
        self.values.append(value)
        self.check()

    def check(self):
        if self.low and self.high and len(self.values) == 2:
            self.low.receive(min(self.values))
            self.high.receive(max(self.values))


class OutputBin(object):
    def __init__(self):
        self.values = []

    def receive(self, value):
        self.values.append(value)

    def __str__(self):
        return 'Bin with ' + ', '.join(map(str, self.values))


bots = defaultdict(Bot)
outputs = defaultdict(OutputBin)


def handle(commands):
    for command in commands:
        terms = command.split()
        if terms[0] == 'value':
            bots[int(terms[5])].receive(int(terms[1]))
        else:  # terms[0] == 'bot'
            lower_dict = bots if terms[5] == 'bot' else outputs
            higher_dict = bots if terms[10] == 'bot' else outputs
            lower = lower_dict[int(terms[6])]
            higher = higher_dict[int(terms[11])]
            bots[int(terms[1])].low = lower
            bots[int(terms[1])].high = higher
            bots[int(terms[1])].check()


handle(open('day10.txt').read().splitlines())

print([k for k, v in bots.items() if sorted(v.values) == [17, 61]][0])

print(reduce(lambda a, b: a * b, [outputs[x].values[0] for x in (0, 1, 2)]))