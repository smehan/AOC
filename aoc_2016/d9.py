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

#TEST_FILE_2 = """(27x12)(20x12)(13x14)(7x10)(1x12)A(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"""
#TEST_FILE_2 = """(27x12)(20x12)(13x14)(7x10)(1x12)A"""
TEST_FILE_2 = """(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"""

TEST_OUTPUT = """ABBBBBCXYZXYZXYZABCBCDEFEFG(1x3)AX(3x3)ABC(3x3)ABCY"""


def get_data(test=False, type=1):
    """
    read in the set of compressed data and return as a list.
    Added guard for test_file 1 or 2.
    :param test: determines whether to use test data or full set
    :param type: int determining whether we are using decompress v1 or v2 for test files
    :return: list of data
    """
    if not test:
        return open('d9.data').readline().strip()
    elif test and type == 2:
        return TEST_FILE_2
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
    return winnow_markers(markers)


def winnow_markers(full_list):
    """
    Removes subsequent compression markers if they are still within the length of the first valid
    marker.
    :param full_list:
    :return:
    """
    for idx in range(len(full_list)):
        if idx == 0:
            out = [full_list[idx]]
        if idx > 0 and full_list[idx][2] > (full_list[idx-1][3] + full_list[idx-1][0] - 1):
            out.append(full_list[idx])
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


def init_stream(s):
    """
    Given a string s read, adds an initial compression marker of (Length(s), 1)
    for symmetry purposes.
    :param s:
    :return:
    """
    init_block = ''.join(['(', str(len(s)), 'x1)'])
    return ''.join([init_block, s])


def divide_marker(s):
    """

    :param s:
    :return:
    """
    pattern = re.compile(r'\((\d+)x(\d+)\)')
    m = re.search(pattern, s)
    return int(m.group(1)), int(m.group(2)), m.span()[0], m.span()[1]


def multiply(s):
    """
    Given a string s, recursively calculate multipliers and lengths of regular chars
    :param s: string of codes
    :return:
    """
    if '(' not in s:
        return len(s)
    elif '(' in s:
        marker = divide_marker(s)
        if marker[2] == 0:
            front = 0
        else:
            front = len(s[0:marker[2]])
        seq = s[marker[3]:marker[0] + marker[3]]
        if s[marker[3]:] == seq:
            remain = ''
        else:
            remain = s[marker[0] + marker[3]:]
        return front + multiply(seq) * marker[1] + multiply(remain)


def multiply_markers(full_list):
    """
    Version 2 multiplies all of the subsequent compressions markers, e.g. (8x2)(3x3) = (3x(2*3))
    (27x12)(20x12)(13x14)(7x10)(1x12)A = A repeated 241920 times.
    (25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN becomes 445 characters long
    :param full_list:
    :return:
    """
    total = len(full_list)
    out = []
    for idx in range(total):
        if total - idx > 0:
            print(full_list[total-idx - 1])
            if full_list[total - idx - 1][3] < full_list[total - idx - 2][2] + full_list[total - idx - 2][0]:
                out.append((full_list[total - idx - 1][0],
                            full_list[total - idx - 1][1] * full_list[total - idx - 2][1],
                            full_list[total - idx - 1][2],
                            full_list[total - idx - 1][3]))
            else:
                out.append(full_list[total - idx - 1])
    print("Bang", out.reverse())
        # if idx == 0:
        #     out = [full_list[idx]]
        # if idx > 0 and full_list[idx][3] < (full_list[idx-1][3] + full_list[idx-1][0] - 1):
        #     print(full_list)


if __name__ == '__main__':
    #print('Decompressed stream has length {}'.format(len(decompress_stream(get_data(test=True)))))
    #print('Test output: {}'.format(len(TEST_OUTPUT)))
    #print(TEST_OUTPUT)
    #print(multiply(init_stream(get_data(test=True, type=2))))
    TEST_FILE_2 = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
    print(multiply(init_stream(TEST_FILE_2)))
    print('Test input was {}'.format(TEST_FILE_2))

