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

TEST_INSTRUCTIONS = ['aaaaa-bbb-z-y-x-123[abxyz]', 'a-b-c-d-e-f-g-h-987[abcde]', 'not-a-real-room-404[oarel]', 'totally-real-room-200[decoy]', 'totally-real-room-aa-yy-d-c-200[decoy]']


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


def sort_freqs(f, n):
    """Sort the frequencies into the top n elements,
    with ties broken by alpha sort"""
    idx = 0
    out = collections.Counter()
    while idx < n:
        remove_k = None
        m = 0
        for k, v in f.items():
            if v > m:
                m = v
                remove_k = k
            if v == m and k < remove_k:
                # tie and k is alpha less than tied key
                m = v
                remove_k = k
        out.update({remove_k: m})
        f.pop(remove_k)
        n -= 1
    return out


def compare_checksum(f, csum):
    """using Counter collection objects to determine frequencies of string,
    then takes the intersection of the string and the checksum to find
    everything in common. If this is equal to the csum collection, return True.
    string Counter object is now sorted in sort_freqs to account for ties"""
    csum_f = collections.Counter(csum)
    f = sort_freqs(f, 5)
    if f & csum_f == csum_f:
        return True
    else:
        return False


if __name__ == '__main__':
    instructions = get_instructions()
    out = 0
    idx = 0
    for r in instructions:
        freq, checksum, sector_id = tokenize_string(r)
        if compare_checksum(freq, checksum):
            out += int(sector_id)
            idx += 1

    print("Total sum of {} valid room sector_ids output is {}. Processed {} codes".format(idx, out, len(instructions)))



