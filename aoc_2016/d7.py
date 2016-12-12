###########################################################
# Copyright (C) 2015-2016 Shawn Mehan <shawn dot mehan at shawnmehan dot com>
# day 7 of AOC_2016
###########################################################
#
#  -*- coding: utf-8 -*-

# standard libs
import re

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
pjxihfkytmmrowclw[savrpenougddqkuq]kfqivyjzfrpfwlftnq[tageosesgmlsmshmv]gjbgdqnwiwnltear[uoxbvzhexqonkbu]ivry
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


def is_aba(s):
    """
    check sequence in s for XYX and returns that sequence if found, or None otherwise.
    :param s:
    :return:
    """
    if s[0] == s[2] and s[0] != s[1]:
        return s
    else:
        return None


def has_bab(seq, s):
    """
    Given an already found XYX in seq, find a reversed YXY in string s.
    Return True if found, False otherwise.
    :param seq:
    :param s:
    :return:
    """
    yxy = ''.join((seq[1], seq[0], seq[1]))
    for match in re.finditer(r'\[[a-z]+\]', s):
        if yxy in match.group(0):
            return True
    return None

def parse_aba(s):
    """
    parses string s for ABA sequence and corresponding [...BAB...], True if both found,
    None otherwise.
    :param s:
    :return:
    """
    valid_aba = False
    bracket = False
    full_s = s
    while len(s) > 2:
        next_seq = s[:3]
        if '[' in next_seq:
            bracket = True
        if ']' in next_seq:
            bracket = False
        aba = is_aba(next_seq)
        if aba and not bracket:
            if has_bab(aba, full_s):
                valid_aba = True
                return valid_aba
        s = s[1:]
    return valid_aba


if __name__ == '__main__':
    data = get_data()
    TLS_count = 0
    SSL_count = 0
    for r in data:
        if parse_abba(r):
            TLS_count += 1
        if parse_aba(r):
            SSL_count += 1
    print('Total TLS count = {}'.format(TLS_count))
    print('Total SSL count = {}'.format(SSL_count))
