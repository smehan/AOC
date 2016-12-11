###########################################################
# Copyright (C) 2015-2016 Shawn Mehan <shawn dot mehan at shawnmehan dot com>
# day 5 of AOC_2016
###########################################################
#
#  -*- coding: utf-8 -*-

# standard libs
import hashlib

# 3rd party libs
import numpy as np

# application libs

"""
The eight-character password for the door is generated one character at a time by finding the
MD5 hash of some Door ID (your puzzle input) and an increasing integer index (starting with 0).

A hash indicates the next character in the password if its hexadecimal representation starts with
five zeroes. If it does, the sixth character in the hash is the next character of the password.

For example, if the Door ID is abc:

The first index which produces a hash that starts with five zeroes is 3231929, which we find by
hashing abc3231929; the sixth character of the hash, and thus the first character of the password, is 1.
5017308 produces the next interesting hash, which starts with 000008f82..., so the second character of
the password is 8.
The third time a hash starts with five zeroes is for abc5278568, discovering the character f.
In this example, after continuing this search a total of eight times, the password is 18f47a30.

Given the actual Door ID, what is the password?

Your puzzle input is ugkcyxxp.

Second lock -

For example, if the Door ID is abc:

The first interesting hash is from abc3231929, which produces 0000015...; so, 5 goes in position 1: _5______.
In the previous method, 5017308 produced an interesting hash; however, it is ignored, because it specifies an invalid position (8).
The second interesting hash is at index 5357525, which produces 000004e...; so, e goes in position 4: _5__e___.
You almost choke on your popcorn as the final character falls into place, producing the password 05ace8e3.
"""

TEST_ID = 'abc'
REAL_ID = 'ugkcyxxp'


def get_hash(s):
    """takes in a string and computes hash (MD5)"""
    h = hashlib.md5(s.encode('utf-8'))
    return h.hexdigest()


def test_hash(s, branch=1):
    """takes in a string hash and tests it for having a valid form
    that provides a password character. If so, returns the character.
    Also, returns the position of that char in second password if branch
    of test is branch 2.
    Otherwise, returns None"""
    if branch == 1:
        if s[:5] == '00000':
            return s[5]
        else:
            return None
    elif branch == 2:
        if s[:5] == '00000':
            try:
                if int(s[5]) in range(8):
                    return s[5], s[6]
                else:
                    return None, None
            except ValueError:
                return None, None
        else:
            return None, None


def output_first_password(s):
    """output function for displaying progress of password, including final output"""
    while len(s) < 8:
        s.append('_')
    print('Your password is {}'.format(''.join(s)))


def output_second_password(s):
    """output function for displaying progress of second password, including final output"""
    while '' in s:
        s[s.index('')] = '_'
    print('Your password is {}'.format(''.join(s)))


def find_password_1(input_id, idx=1):
    """uses first algorithm to find password from hashes on input_id"""
    solutions = []
    while len(solutions) < 8:
        out = test_hash(get_hash(''.join([input_id, str(idx)])))
        if out is not None:
            solutions.append(out)
            output_first_password(solutions[:])
        idx += 1


def find_password_2(input_id, idx=1):
    """uses second algorithm to find password from hashes on input_id"""
    solutions2 = ['', '', '', '', '', '', '', '']
    while '' in solutions2:
        pos, char = test_hash(get_hash(''.join([input_id, str(idx)])), branch=2)
        if pos is not None and solutions2[int(pos)] == '':
            solutions2[int(pos)] = char
            output_second_password(solutions2[:])
        idx += 1


if __name__ == '__main__':
    find_password_1(REAL_ID)
    find_password_2(REAL_ID)

