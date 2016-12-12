###########################################################
# Copyright (C) 2015-2016 Shawn Mehan <shawn dot mehan at shawnmehan dot com>
# day 8 of AOC_2016
###########################################################
#
#  -*- coding: utf-8 -*-

# standard libs
import re

# 3rd party libs
import numpy as np

# application libs


TEST_DATA = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1"""

TEST_SCREEN_RES = (3, 7)

REAL_SCREEN_RES = (6, 50)


def make_screen(test=False):
    """
    Creates an array representing the pixels in the screen.
    :param test: determines whether to make a test size screen or real size.
    :return: the array to use.
    """
    if not test:
        return np.zeros(REAL_SCREEN_RES, dtype=np.int16)
    else:
        return np.zeros(TEST_SCREEN_RES, dtype=np.int16)


def get_instructions(test=False):
    """
    read in the set of instructions and return as a list
    :param test: determines whether to use test instructions of full set
    :return: list of instructions
    """
    if not test:
        return [line.strip() for line in open('d8.data').readlines()]
    else:
        return [line.strip() for line in TEST_DATA.split('\n')]


def create_rect(screen, s):
    """
    Given size of a rectangle in s, update state of screen to reflect new state
    :param screen:
    :param s: an instruction to build a rectangle in COL x ROW order
    :return:
    """
    m = re.search(r'(\d+)x(\d+)', s)
    a, b = int(m.group(2)), int(m.group(1))
    print('{} x {}'.format(a, b))
    for i in range(a):
        for j in range(b):
            screen[i, j] = 1
    return screen


def rotate_row(screen, s):
    """
    Given a row and shift distance in s, update screen to reflect new state
    :param screen:
    :param s:
    :return:
    """


def update_screen(screen, instruction):
    """
    Given an instruction, transform the state of the screen and return.
    :param screen:
    :param instruction:
    :return:
    """
    print(instruction)
    if 'rect' in instruction:
        screen = create_rect(screen, instruction)
    return screen


def count_on(screen):
    """
    Given a screen repr, count how many pixels are on, i.e., 1
    :param screen:
    :return:
    """
    return sum(e for e in screen.flat)


if __name__ == '__main__':
    test = True
    scr = make_screen(test)
    instructions = get_instructions(test)
    for r in instructions:
        scr = update_screen(scr, r)
    print('Total pixels turned on is {}'.format(count_on(scr)))
    print(scr)
