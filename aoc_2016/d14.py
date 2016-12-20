###########################################################
# Copyright (C) 2015-2016 Shawn Mehan <shawn dot mehan at shawnmehan dot com>
# day 14 of AOC_2016
###########################################################
#
#  -*- coding: utf-8 -*-

# standard libs
import hashlib
from collections import deque

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
hash_history = {}


def make_hash(salt, n):
    """
    given a salt and an int n, build an md5 hash and return it
    :param salt:
    :param n: index to add to end of hash.
    :return:
    """
    if n is None:
        n = ''
    return hashlib.md5(''.join([salt, str(n)]).encode('utf-8')).hexdigest()


def find_first_triple(h):
    """
    Given hash h, find the first triple occurrence of a char.
    :param h: str
    :return: the character repeating or None
    """
    for i in range(len(h) - 2):
        if h[i] == h[i + 1] == h[i + 2]:
            return h[i]
    else:
        return None


def find_five(h, c):
    """
    Search hash h for five contiguous occurrences of c and return True, False otherwise.
    :param h:
    :param c:
    :return:
    """
    return 5 * c in h


def make_stretch_has(salt, n):
    """
    additional processing on salt+n to use result of hash to make a new
    hash, repeatedly. Stores previously seen hashes to reduce computes.
    :param salt:
    :param n:
    :return:
    """
    h = make_hash(salt, n)
    if salt + n in hash_history:
        print('Seen {}'.format(salt + n))
        return hash_history[salt + n]
    for _ in range(2016):
        h = make_hash(h, None)
    hash_history[salt + n] = h
    return h


def is_key(salt, idx, part=1):
    """
    Given a salt and an index to combine, computes the hash,
    finds the triple seq and then tests for five seq with same
    char. Also uses stretch key algorithm for part 2.
    :param salt:
    :param idx:
    :param part:
    :return:
    """
    if part == 1:
        h = make_hash(salt, str(idx))
    else:
        h = make_stretch_has(salt, str(idx))
    c = find_first_triple(h)
    if c:
        for i in range(1, 1001):
            if part == 1:
                h = make_hash(salt, str(idx + i))
            else:
                h = make_stretch_has(salt, str(idx + i))
            if find_five(h, c):
                return True
    return False


def key_generator(salt, part):
    idx = 0
    while True:
        if is_key(salt, idx, part):
            yield idx
        idx += 1


def sixty_fourth_key(salt, part=1):
    g = key_generator(salt, part)
    for x in range(TARGET):
        c = next(g)
    return c


if __name__ == '__main__':
    good_keys = deque()
    all_keys = []
    search_idx = 0
    suffix = 0

    assert not is_key(TEST_SALT, 18)
    assert is_key(TEST_SALT, 39)
    assert is_key(TEST_SALT, 92)
    assert sixty_fourth_key(TEST_SALT) == 22728

    print("Part 1: {}".format(sixty_fourth_key(SALT)))

    print('Attempting stretch_keys ...')
    assert not is_key(TEST_SALT, 5, 2)
    assert is_key(TEST_SALT, 10, 2)
    assert is_key(TEST_SALT, 22551, 2)
    print('Now seeking main target ...')
    print("Part 2: %s" % sixty_fourth_key(SALT, part=2))



