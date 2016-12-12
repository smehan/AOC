###########################################################
# Copyright (C) 2015-2016 Shawn Mehan <shawn dot mehan at shawnmehan dot com>
# day 9 of AOC_2016
###########################################################
#
#  -*- coding: utf-8 -*-

# standard libs
import re

# 3rd party libs
import numpy as np

# application libs

"""ADVENT contains no markers and decompresses to itself with no changes, resulting in a decompressed length of 6.
A(1x5)BC repeats only the B a total of 5 times, becoming ABBBBBC for a decompressed length of 7.
(3x3)XYZ becomes XYZXYZXYZ for a decompressed length of 9.
A(2x2)BCD(2x2)EFG doubles the BC and EF, becoming ABCBCDEFEFG for a decompressed length of 11.
(6x1)(1x3)A simply becomes (1x3)A - the (1x3) looks like a marker, but because it's within a data section of another marker, it is not treated any differently from the A that comes after it. It has a decompressed length of 6.
X(8x2)(3x3)ABCY becomes X(3x3)ABC(3x3)ABCY (for a decompressed length of 18), because the decompressed data from the (8x2) marker (the (3x3)ABC) is skipped and not processed further."""

TEST_FILE = """A(1x5)BC(3x3)XYZA(2x2)BCD(2x2)EFG(6x1)(1x3)AX(8x2)(3x3)ABCY"""

TEST_OUTPUT = """ABBBBBCXYZXYZXYZABCBCDEFEFG(1x3)AX(3x3)ABC(3x3)ABCY"""


def get_data(test=False):
    """
    read in the set of compressed data and return as a list
    :param test: determines whether to use test data or full set
    :return: list of data
    """
    if not test:
        return open('d9.data').readline().strip()
    else:
        return TEST_FILE


def get_markers(s):
    """
    Pull out all valid markers in string, after stripping out any markers
    invalidated by being in the shadow of a previous, valid marker.
    :param s:
    :return:
    """
    pattern = re.compile(r'\((\d+)x(\d+)\)')
    markers = []
    for m in re.finditer(pattern, s):
        markers.append((int(m.group(1)), int(m.group(2)), m.span()[0], m.span()[1]))
    for idx, tup in enumerate(markers):
        if idx == 0:
            out = [markers[idx]]
        if idx > 0 and markers[idx][2] > (markers[idx-1][3] + markers[idx-1][0] - 1):
            out.append(markers[idx])
    return out


def marker_starts(markers):
    return (pos[2] for pos in markers)


def expand_marker(idx, s, markers):
    """

    :param idx:
    :param s:
    :param markers:
    :return: a new seq with expansion, next_pos to start copying again
    """
    for m in markers:
        if idx == m[2]:
            return s[m[3]:m[3] + m[0]] * m[1], m[3] + m[0]


def decompress_stream(s):
    """
    Given string s, parse looking for valid compression markers.
    Expand them and return a new, decompressed stream.
    marker = (LengthxFreq)
    :param s:
    :return:
    """
    new_stream = ''
    next_pos = 0
    markers = get_markers(s)
    for idx, char in enumerate(s):
        if idx < next_pos:
            continue
        if idx in marker_starts(markers):
            seq, next_pos = expand_marker(idx, s, markers)
            new_stream += seq
        else:
            new_stream += char
    print(s)
    print(new_stream)
    return new_stream

if __name__ == '__main__':
    print('Decompressed stream has length {}'.format(len(decompress_stream(get_data()))))
    # print('Test output: {}'.format(len(TEST_OUTPUT)))
    # print(TEST_OUTPUT)

