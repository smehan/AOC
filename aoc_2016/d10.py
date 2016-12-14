###########################################################
# Copyright (C) 2015-2016 Shawn Mehan <shawn dot mehan at shawnmehan dot com>
# day 10 of AOC_2016
###########################################################
#
#  -*- coding: utf-8 -*-

# standard libs
from re import compile
from operator import mul, itemgetter
from functools import reduce
from itertools import tee, filterfalse, chain

# 3rd party libs
import numpy as np

# application libs


TEST_DATA = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2"""

"""
Initially, bot 1 starts with a value-3 chip, and bot 2 starts with a value-2 chip and a value-5 chip.
Because bot 2 has two microchips, it gives its lower one (2) to bot 1 and its higher one (5) to bot 0.
Then, bot 1 has two microchips; it puts the value-2 chip in output 1 and gives the value-3 chip to bot 0.
Finally, bot 0 has two microchips; it puts the 3 in output 2 and the 5 in output 0.
In the end, output bin 0 contains a value-5 microchip, output bin 1 contains a value-2 microchip,
and output bin 2 contains a value-3 microchip.

In this configuration, bot number 2 is responsible for comparing value-5 microchips with value-2 microchips.
"""


value_regex = compile('value (\d+) goes to (bot \d+)')
botcmd_regex = compile('(bot \d+) gives low to ((?:output|bot) \d+) and high to ((?:output|bot) \d+)')


def get_data(test=False):
    """
    Returns list of lines in data file if Test is False, Test data otherwise.
    :param test:
    :return:
    """
    if not test:
        return [line.strip() for line in open("d10.data").readlines()]
    else:
        return [line.strip() for line in TEST_DATA.split('\n')]


def parse_lines(lines, regex):
    return [regex.match(line).groups() for line in lines]


def partition(pred, iterable):
    """
    Creates a positive and negative sub_iter out of iter branching on pred
    :param pred:
    :param iterable:
    :return:
    """
    t1, t2 = tee(iterable)
    return filterfalse(pred, t1), filter(pred, t2)


def define_bot(bot, low, high, bins):
    def dist_a(a):
        def dist_b(b):
            h, l        = max(a, b), min(a, b)
            bins[high]  = bins[high](h)
            bins[low]   = bins[low](l)
            return h, l
        return dist_b
    return dist_a


def bot_eval(inputs, cmds, bins):
    for bot, low, high in cmds:
        bins[bot] = define_bot(bot, low, high, bins)

    for val, bot in inputs:
        bins[bot] = bins[bot](int(val))


def get_outputs(bins):
    outputBins = ((k, v) for k, v in bins.items() if k.startswith("output"))
    return [v for k, v in sorted(outputBins, key=lambda x: int(x[0].split(" ")[-1]))]


def day10(data):
    inputs, cmds = partition(lambda s: s.startswith("bot"), data)
    inputs, cmds = parse_lines(inputs, value_regex), parse_lines(cmds, botcmd_regex)

    bins = {x:lambda y: y for x in chain.from_iterable(cmds)}
    bot_eval(inputs, cmds, bins)

    outputs = get_outputs(bins)
    return {v:k for k, v in bins.items()}[(61, 17)], reduce(mul, outputs[:3], 1)


if __name__ == '__main__':
    print(day10(get_data()))
