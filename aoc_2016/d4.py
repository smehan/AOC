###########################################################
# Copyright (C) 2015-2016 Shawn Mehan <shawn dot mehan at shawnmehan dot com>
# day 4 of AOC_2016
###########################################################
#
#  -*- coding: utf-8 -*-

# standard libs
import collections

# 3rd party libs
import numpy as np

# application libs


"""A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order,
with ties broken by alphabetization. For example:

aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a
tie between x, y, and z, which are listed alphabetically.

a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each),
the first five are listed alphabetically.

not-a-real-room-404[oarel] is a real room.

totally-real-room-200[decoy] is not.

Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?"""

TEST_INSTRUCTIONS = ['aaaaa-bbb-z-y-x-123[abxyz]', 'a-b-c-d-e-f-g-h-987[abcde]', 'not-a-real-room-404[oarel]', 'totally-real-room-200[decoy]']


def get_instructions():
    """read data file and return a list of all lines"""
    return [line.strip() for line in open('d4.data', 'r').readlines()]


def tokenize_string(s):
    """break input string into principal components for processing"""
    front, csum = s.replace(']', '').split('[')
    units = front.split('-')
    sid = units[-1]
    f = collections.Counter((c for u in units[:-1] for c in u))
    return f, csum, sid


def compare_checksum(f, csum):
    """compare the freq values of first five keys to csum elements"""
    print('Hey, ', f.items(), f.most_common(5))
    csum_f = collections.Counter(csum)
    if f & csum_f == csum_f:
        return True
    else:
        return False


if __name__ == '__main__':
    instructions = get_instructions()
    test_instructions = TEST_INSTRUCTIONS
    out = 0
    for r in test_instructions:
        freq, checksum, sector_id = tokenize_string(r)
        if compare_checksum(freq, checksum):
            out += int(sector_id)

    print("Total sector_id output is {}".format(out))



