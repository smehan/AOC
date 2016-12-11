###########################################################
# Copyright (C) 2015-2016 Shawn Mehan <shawn dot mehan at shawnmehan dot com>
# day 6 of AOC_2016
###########################################################
#
#  -*- coding: utf-8 -*-

# standard libs
import collections

# 3rd party libs
import numpy as np

# application libs


TEST_DATA = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""


def get_data(test=False):
    """
    returns a list of transmission strings to parse from data file, or uses
    test data if test is True.
    :param test: Boolean to use test data or not
    :return: list of strings
    """
    if not test:
        return [line.strip('\n') for line in open('d6.data').readlines()]
    else:
        return TEST_DATA.split('\n')


def get_cols(data):
    """
    Given a list of strings, takes each row and splits each row into columns, e.g.
    [afgter, astwqe] turns into cols = [1:[a, a], 2:[f, s], ...]
    :param data: list of strings
    :return: dict of [col: [chars in col]]
    """
    out = {}
    for r in data:
        for c in range(len(r)):
            try:
                out[c + 1].append(r[c])
            except KeyError:
                out[c + 1] = [r[c]]
    return out


def get_message(data, kind='most_common'):
    """
    Given a dictionary of {col: [e1, e2, ...], ...}, computes a Counter
    object for each column, and then outputs the most_common element in each col.
    :param data: {col: [e1, e2, ...], ...}
    :return:
    """
    if kind == 'most_common':
        for k, v in data.items():
            count = collections.Counter(v)
            print(count.most_common(1))
    else:
        for k, v in data.items():
            count = collections.Counter(v)
            print(count.most_common()[-1])


if __name__ == '__main__':
    chars = get_cols(get_data(test=False))
    get_message(chars, kind='most_common')
    get_message(chars, kind='least_common')
