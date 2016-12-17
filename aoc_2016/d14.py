###########################################################
# Copyright (C) 2015-2016 Shawn Mehan <shawn dot mehan at shawnmehan dot com>
# day 14 of AOC_2016
###########################################################
#
#  -*- coding: utf-8 -*-

# standard libs
import hashlib
from collections import deque
import re

# 3rd party libs
import numpy as np

# application libs

"""
A hash is a key only if:

It contains three of the same character in a row, like 777. Only consider the first such triplet in a hash.
One of the next 1000 hashes in the stream contains that same character five times in a row, like 77777.
Considering future hashes for five-of-a-kind sequences does not cause those hashes to be skipped; instead, regardless of whether the current hash is a key, always resume testing for keys starting with the very next hash.

For example, if the pre-arranged salt is abc:

The first index which produces a triple is 18, because the MD5 hash of abc18 contains ...cc38887a5.... However, index 18 does not count as a key for your one-time pad, because none of the next thousand hashes (index 19 through index 1018) contain 88888.
The next index which produces a triple is 39; the hash of abc39 contains eee. It is also the first key: one of the next thousand hashes (the one at index 816) contains eeeee.
None of the next six triples are keys, but the one after that, at index 92, is: it contains 999 and index 200 contains 99999.
Eventually, index 22728 meets all of the criteria to generate the 64th key.
So, using our example salt of abc, index 22728 produces the 64th key.
"""

TEST_SALT = 'abc'
TARGET = 64
SALT = 'cuanljph'


def make_hash(salt, n):
    """
    given a salt and an int n, build an md5 hash and return it
    :param salt:
    :param n:
    :return:
    """
    return hashlib.md5(''.join([salt, str(n)]).encode('utf-8')).hexdigest()


def find_first_triple(h):
    """
    Given hash h, find the first triple occurrence of a char.
    :param h: str
    :return: the character repeating or None
    """
    i = 0
    while i < len(h) - 2:
        if h[i] == h[i + 1] == h[i + 2]:
            return h[i]
        i += 1
    else:
        return ''


def find_five(h, c):
    """
    Search hash h for five contiguous occurrences of c and return True, False otherwise.
    :param h:
    :param c:
    :return:
    """
    return 5 * c in h


if __name__ == '__main__':
    good_keys = deque()
    all_keys = []
    search_idx = 0
    suffix = 0
    while len(good_keys) < TARGET:
        key = make_hash(TEST_SALT, suffix)
        all_keys.append(key)
        if len(all_keys) > 1000:
            triple = find_first_triple(all_keys[len(all_keys) - 1000])
            if triple != '':
                for i in range(999, -1, -1):
                    if find_five(all_keys[i], triple):
                        print('Target', all_keys[len(all_keys) - 1000])
                        good_keys.append(all_keys[len(all_keys) - 1000])
                        break

        suffix += 1
        if suffix % 1000 == 0:
            print('Trying hash {}: '.format(suffix))
        if len(good_keys) > 0:
            print(key, good_keys[len(good_keys) - 1])
    else:
        print('Found the {} key: {}'.format(TARGET, good_keys[len(good_keys) - 1]))
        print(good_keys)
        for idx, e in enumerate(good_keys):
            print(idx, all_keys.index(e))

