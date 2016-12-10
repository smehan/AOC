###########################################################
# Copyright (C) 2015-2016 Shawn Mehan <shawn dot mehan at shawnmehan dot com>
# day 4 of AOC_2016
###########################################################
#
#  -*- coding: utf-8 -*-

# standard libs
import collections
import string

# 3rd party libs
import numpy as np

# application libs


"""A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order,
with ties broken by alphabetization. For example:

Of the real rooms from the list below, the sum of their sector IDs is 1514."""

TEST_INSTRUCTIONS = ['aaaaa-bbb-z-y-x-123[abxyz]', 'a-b-c-d-e-f-g-h-987[abcde]', 'not-a-real-room-404[oarel]',
                     'totally-real-room-200[decoy]', 'totally-real-room-aa-yy-d-c-200[decoy]',
                     'a-b-c-d-e-f-g-h-987[agcde]']


def get_instructions():
    """read data file and return a list of all lines"""
    return [line.strip() for line in open('d4.data', 'r').readlines()]


def tokenize_string(s):
    """break input string into principal components for processing"""
    front, csum = s.replace(']', '').split('[')
    units = front.split('-')
    sid = units[-1]
    f = collections.Counter((c for u in units[:-1] for c in u))
    room_code = [w for w in units[:-1]]
    return f, csum, sid, room_code


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
    if sort_freqs(f, 5) & csum_f == csum_f:
        return True
    else:
        return False


def shift_decrypt(word_list, n):
    """takes a list of strings and rotates each letter in each word by n.
    Checks to see if any of the decoded room names have North in them,
    and prints those and their ids."""
    # chars lie between (97, 122)
    shift_by = n % 26
    LETTERS = list(string.ascii_lowercase)
    out = ''
    for w in word_list:
        word = []
        for c in w:
            if LETTERS.index(c) + shift_by < 26:
                word.append(LETTERS[LETTERS.index(c) + shift_by])
            else:
                word.append(LETTERS[LETTERS.index(c) + shift_by - len(LETTERS)])
        out += ''.join(word) + ' '
    if 'north' in out:
        print('{} in room {}'.format(out.strip(), n))


if __name__ == '__main__':
    instructions = get_instructions()
    out = 0
    idx = 0
    for r in instructions:
        freq, checksum, sector_id, room_code = tokenize_string(r)
        if compare_checksum(freq, checksum):
            out += int(sector_id)
            idx += 1
        shift_decrypt(room_code, int(sector_id))

    print("Total of {} valid room sector_ids sum to {}. Processed {} codes...".format(idx, out, len(instructions)))



