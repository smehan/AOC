###########################################################
# Copyright (C) 2015-2016 Shawn Mehan <shawn dot mehan at shawnmehan dot com>
# day 7 of AOC_2016
###########################################################
#
#  -*- coding: utf-8 -*-

# standard libs

# 3rd party libs
import numpy as np

# application libs

"""
abba[mnop]qrst supports TLS (abba outside square brackets).
abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
"""

""" For SSL
aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
"""

TEST_DATA = ['abba[mnop]qrst', 'abcd[bddb]xyyx', 'aaaa[qwer]tyui', 'ioxxoj[asdfgh]zxcvbn',
             'aba[bab]xyz', 'xyx[xyx]xyx', 'aaa[kek]eke', 'zazbz[bzb]cdb']


def get_data(test=False):
    """
    Assemble data for parsing. If test=True, use TEST_DATA, otherwise, read in from file.
    :param test:
    :return:
    """
    if test:
        return TEST_DATA
    else:
        return [line.strip() for line in open('d7.data').readlines()]


def is_abba(seq):
    """
    Check string seq for ABBA character and return True if found, otherwise False
    :param seq:
    :return:
    """
    if seq == seq[::-1] and seq[0] != seq[1]:
        print(seq)
        return True
    else:
        return False


def parse_abba(s):
    """
    parses string s for XXYY sequence. Returns True if found, None otherwise.
    :param s:
    :return:
    """
    valid_abba = False
    bracket = False
    while len(s) > 3:
        next_seq = s[:4]
        if '[' in next_seq:
            bracket = True
        if ']' in next_seq:
            bracket = False
        if is_abba(next_seq) and bracket:
            return False
        if is_abba(next_seq) and not bracket:
            valid_abba = True
        s = s[1:]
    return valid_abba


if __name__ == '__main__':
    data = get_data()
    count = 0
    for r in data:
        if parse_abba(r):
            count += 1
            print('valid IP7: {}'.format(r))
    print('Total count = {}'.format(count))
