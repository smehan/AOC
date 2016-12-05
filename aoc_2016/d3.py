###########################################################
# Copyright (C) 2015-2016 Shawn Mehan <shawn dot mehan at shawnmehan dot com>
# day 3 of AOC_2016
###########################################################
#
#  -*- coding: utf-8 -*-

# standard libs

# 3rd party libs
import numpy as np

# application libs

test_data = """
5 10 25
"""


def split_row(r):
    """takes string as row and returns tuple (a, b, c)"""
    r = r.strip()
    return int(r.split()[0]), int(r.split()[1]), int(r.split()[2])


def get_sides(data):
    """given a list of lines each with three ints, will
    create a list of triples"""
    out = []
    for r in data:
        if r == '':
            continue
        else:
            out.append(split_row(r))
    return out


def left_shift(tup, n=1):
    """left shift eleemnts of a tuple by n"""
    try:
        n = n % len(tup)
    except ZeroDivisionError:
        return tuple()
    return tup[n:] + tup[0:n]


def is_triangle(sides):
    """given tuple with three sides of a possible triangle,
    determines if all three obey rule a + b > c
    :param sides: tuple (int, int, int)
    return: True if sides obey sum rule, False otherwise
    """
    if sides[0] + sides[1] > sides[2]:
        return True
    else:
        return False


def build_tuple(tup1, tup2, tup3, row):
    """takes a row and three tuples and build the next set of numbers in the tuples from the row. """
    # tuple passed is len = 0
    if len(tup1) == 0:
        return (row[0], 0), (row[1], 0), (row[2], 0)
    # tuple passed is len = 2 and t[1] = 0
    if len(tup1) == 2 and tup1[1] == 0:
        return (tup1[0], row[0]), (tup2[0], row[1]), (tup3[0], row[2])
    # tuple passed is len = 2 and t[1] != 0
    if len(tup1) == 2 and tup1[1] != 0:
        return (tup1[0], tup1[1], row[0]), (tup2[0], tup2[1], row[1]), (tup3[0], tup3[1], row[2])


if __name__ == '__main__':
    count = 0
    #data = get_sides(test_data)
    data = get_sides([line.strip() for line in open('d3.data').readlines()])
    for row in data:
        if is_triangle(row) and is_triangle(left_shift(row)) and is_triangle(left_shift(row, 2)):
            count += 1
    print("There are {} possible tiangles in the first pass.".format(count))
    count = 0
    tri1, tri2, tri3 = (), (), ()
    for idx, row in enumerate(data):
        tri1, tri2, tri3 = build_tuple(tri1, tri2, tri3, row)
        if (idx +1) % 3 == 0:
            if is_triangle(tri1) and is_triangle(left_shift(tri1)) and is_triangle(left_shift(tri1, 2)):
                count += 1
            if is_triangle(tri2) and is_triangle(left_shift(tri2)) and is_triangle(left_shift(tri2, 2)):
                count += 1
            if is_triangle(tri3) and is_triangle(left_shift(tri3)) and is_triangle(left_shift(tri3, 2)):
                count += 1
            tri1, tri2, tri3 = (), (), ()
    print("There are {} possible tiangles in the second pass.".format(count))

