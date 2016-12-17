###########################################################
# Copyright (C) 2015-2016 Shawn Mehan <shawn dot mehan at shawnmehan dot com>
# day 13 of AOC_2016
###########################################################
#
#  -*- coding: utf-8 -*-

# standard libs

# 3rd party libs
import numpy as np

# application libs

"""
Find x*x + 3*x + 2*x*y + y + y*y.
Add the office designer's favorite number (your puzzle input).
Find the binary representation of that sum; count the number of bits that are 1.
If the number of bits that are 1 is even, it's an open space.
If the number of bits that are 1 is odd, it's a wall.
"""

"""TEST
  0123456789
0 .#.####.##
1 ..#..#...#
2 #....##...
3 ###.#.###.
4 .##..#..#.
5 ..##....#.
6 #...##.###
"""

TEST_FAV = 10
TEST_GRID = (7, 10)

FAV = 1362
GRID = (40, 40)


def make_grid(grid_size=(10, 10)):
    """
    Creates an array representing the office.
    :param grid_size: office grid size, tuple.
    :return: the array to use.
    """
    return np.zeros(grid_size, dtype=np.int16)


def is_even(bin_num):
    """
    Given a binary number in a str representation, returns True if the number of 1 bits is
    even, otherwise returns False.
    :param bin_num:
    :return:
    """
    if list(bin_num).count('1') % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    grid = make_grid(TEST_GRID)
    fn = TEST_FAV
    for y in range(1, grid.shape[0] + 1):
        for x in range(1, grid.shape[1] + 1):
            # print('Examining ({}, {})'.format(y, x))
            dec = x*x + 3*x + 2*x*y + y + y*y + fn
            bn = format(dec, 'b')
            if is_even(bn):
                grid[y - 1, x - 1] = 0
            else:
                grid[y - 1, x - 1] = 1
    print(grid)

