###########################################################
# Copyright (C) 2015-2016 Shawn Mehan <shawn dot mehan at shawnmehan dot com>
# day 15 of AOC_2016
###########################################################
#
#  -*- coding: utf-8 -*-

# standard libs
import itertools

# 3rd party libs
import numpy as np

# application libs

"""
Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
If you press the button exactly at time=0, the capsule would start to fall; it would reach the
first disc at time=1. Since the first disc was at position 4 at time=0, by time=1 it has ticked
one position forward. As a five-position disc, the next position is 0, and the capsule falls through the slot.

Then, at time=2, the capsule reaches the second disc. The second disc has ticked forward two
positions at this point: it started at position 1, then continued to position 0, and finally ended
up at position 1 again. Because there's only a slot at position 0, the capsule bounces away.

If, however, you wait until time=5 to push the button, then when the capsule reaches each disc,
the first disc will have ticked forward 5+1 = 6 times (to position 0), and the second disc will have
ticked forward 5+2 = 7 times (also to position 0). In this case, the capsule would fall through the discs
and come out of the machine.
"""

"""{DISC_nbr: (current_pos, nbr_slots)"""
TEST_ARRAY = {1: (4, 5),
              2: (1, 2)}

states = {}


def get_data(test=False):
    """
    initialize disc dict with test or general information.
    :param test:
    :return: dict of disc states for current time slice.
    """
    if test:
        return TEST_ARRAY


def is_solved(states):
    """
    tests disc array to see if
    :param discs:
    :return:
    """
    # how many discs in the array
    array_length = len(states[0])
    for s in states:
        print('Time step: {}'.format(s))
        if states[s][1][0] == 0:
            print('This step has first disc solved.')
            for d in range(array_length):
                if not all(states[s][d + 1]):
                    print('Disc: {} has {}.'.format(d + 1, states[s][d + 1]))


def update_discs(discs):
    """
    move all of the discs one position for next time step
    :param discs:
    :return:
    """
    new_discs = {}
    for disc, arrangement in discs.items():
        new_discs[disc] = ((arrangement[0] + 1) % (arrangement[1]), arrangement[1])
    return(new_discs)


def ball_drop(discs):
    """
    controls the movement of disks and ball in time-steps.
    :param discs: dict representing state of discs(t).
    :return:
    """
    for step in range(100):
        states[step] = discs
        print('Time step {}.'.format(step))
        discs = update_discs(discs)
    is_solved(states)


def parse_input(inp):
    inp = map(lambda x: x.split(" "), inp)
    lines = [(int(l[3]), int(l[-1][:-2])) for l in inp]
    print(lines)


def check_solution(setup, time):
    return all((setup[i][1] + time + i + 1) % setup[i][0] == 0
               for i in range(len(setup)))


def get_first_drop_time(init):
    for i in itertools.count():
        if check_solution(setup, i):
            return i


if __name__ == '__main__':
    assert parse_input('Disc 5 has 19 positions; at time=0, it is at position 9.') == (19, 9)
    print('bang')
    #assert parse_input('Disc #6 has 7 positions; at time=0, it is at position 0.') == (7, '0')
    with open('d15.data', 'r') as fh:
        setup = parse_input(fh.readlines())
        print("Part 1: {}".format(get_first_drop_time(setup)))
        setup.append((11, 0))
        print("Part 2: {}".format(get_first_drop_time(setup)))
    ball_drop(get_data(test=True))
