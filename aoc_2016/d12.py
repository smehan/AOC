###########################################################
# Copyright (C) 2015-2016 Shawn Mehan <shawn dot mehan at shawnmehan dot com>
# day 12 of AOC_2016
###########################################################
#
#  -*- coding: utf-8 -*-

# standard libs
import re
from collections import OrderedDict

# 3rd party libs
import numpy as np

# application libs


"""
The assembunny code you've extracted operates on four registers (a, b, c, and d) that start at 0 and can hold any integer. However, it seems to make use of only a few instructions:

cpy x y copies x (either an integer or the value of a register) into register y.
inc x increases the value of register x by one.
dec x decreases the value of register x by one.
jnz x y jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.
The jnz instruction moves relative to itself: an offset of -1 would continue at the previous instruction, while an offset of 2 would skip over the next instruction.
"""

TEST_DATA = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""


cpy_regex = re.compile('cpy ((?:a|b|c|d|\d+)) ((?:a|b|c|d))')
inc_regex = re.compile('inc ((?:a|b|c|d))')
dec_regex = re.compile('dec ((?:a|b|c|d))')
jnz_regex = re.compile('jnz ((?:a|b|c|d|\d+)) (-?\d+)')


def get_data(test=False):
    """
    Returns list of lines in data file if Test is False, Test data otherwise.
    :param test:
    :return:
    """
    if not test:
        return OrderedDict(enumerate((line.strip() for line in open("d12.data").readlines())))
    else:
        return OrderedDict(enumerate((line.strip() for line in TEST_DATA.split('\n'))))


def parse_line(data, regex):
    """
    return captured groups in a tuple, dependent on regex match.
    :param data:
    :param regex:
    :return:
    """
    return regex.match(data).groups()


def is_reg(v):
    """
    tests if v is a valid register
    :param v:
    :return: True if valid, false otherwise
    """
    if v in ('a', 'b', 'c', 'd'):
        return True
    else:
        return False


def do_cpy(r, k):
    """
    cpy 1 a or cpy a c
    :param r:
    :param k:
    :return:
    """
    v, reg = parse_line(r, cpy_regex)
    if is_reg(v):
        registers[reg] = registers[v]
    else:
        registers[reg] = int(v)
    return k + 1


def do_inc(r, k):
    """

    :param r:
    :param k:
    :return:
    """
    reg = parse_line(r, inc_regex)
    registers[reg[0]] = int(registers[reg[0]]) + 1
    return k + 1


def do_dec(r, k):
    """

    :param r:
    :param k:
    :return:
    """
    reg = parse_line(r, dec_regex)
    registers[reg[0]] = int(registers[reg[0]]) - 1
    return k + 1


def do_jnz(r, idx, length):
    """

    :param r:
    :param idx:
    :return:
    """
    reg, v = parse_line(r, jnz_regex)
    if is_reg(reg):
        if registers[reg[0]] == 0:
            return idx + 1
        else:
            return idx + int(v)
    elif int(reg) == 0:
        return idx + 1
    else:
        return idx + int(v)


def process_instructions(data):
    """

    :param data:
    :return:
    """
    current_idx = 0
    step = 1
    while current_idx < len(data):
        k, r = current_idx, data[current_idx]
        if r.startswith('cpy'):
            current_idx = do_cpy(r, k)
        elif r.startswith('inc'):
            current_idx = do_inc(r, k)
        elif r.startswith('dec'):
            current_idx = do_dec(r, k)
        elif r.startswith('jnz'):
            current_idx = do_jnz(r, k, len(data))
        step += 1
    else:
        print('Completed after {} steps'.format(step))


if __name__ == '__main__':
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    process_instructions(get_data())
    print('Part 1: a = {}'.format(registers['a']))
    registers = {'a': 0, 'b': 0, 'c': 1, 'd':0}
    process_instructions(get_data())
    print('Part 2: a = {}'.format(registers['a']))