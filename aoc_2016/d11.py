###########################################################
# Copyright (C) 2015-2016 Shawn Mehan <shawn dot mehan at shawnmehan dot com>
# day 11 of AOC_2016
###########################################################
#
#  -*- coding: utf-8 -*-

# standard libs
from collections import deque, namedtuple

# 3rd party libs
import numpy as np

# application libs

########################
# initialization
########################

test_components = []
components = ['prg', 'prm', 'cog', 'com', 'rug', 'rum', 'plg', 'plm', 'cug', 'cum']

test_layout = [2, 1, 3, 1]
State = namedtuple('State', ['floors', 'elevator', 'step', 'parent'])


def expand(state):
    """
    expand possible nodes from current node.
    :param state:
    :return:
    """
    g = [sum(1 for v in state.floors[::2] if v == fn) for fn in range(1, 5)]
    m = [sum(1 for v in state.floors[1::2] if v == fn) for fn in range(1, 5)]
    return ''.join(map(str, g + m)) + str(state.elevator)


def is_solved(state):
    """
    checks for whether state of node is solution.
    :param state: namedtuple for present state node being checked.
    :return: True if all components on 4th floor.
    """
    return all(i == 4 for i in state.floors)


def is_valid(node):
    """
    determine if present node is a valid node.
    :param node:
    :return: True if valid, False otherwise
    """
    return True


def solver(initial_layout):
    """
    Drives for search of state-state space to find solutions.
    :param initial_layout: floors for each of the components at init.
    :return:
    """
    solver_q = deque()
    # ('State', ['floors', 'elevator', 'step', 'parent'])
    solver_q.append(State(initial_layout, 1, 0, None))
    seen = set()
    node_count = 1
    while solver_q:
        state = solver_q.popleft()
        print(expand(state))
        for idx in range(len(state.floors)):
            i = state.floors[idx]
            if i != state.elevator:  # skip as item not in elevator
                continue
            state.floors[idx] -= 1
            solver_q.append(State(list(state.floors),
                                 state.elevator - 1,
                                 state.step + 1,
                                 state))
            state.floors[idx] += 2
            solver_q.append(State(list(state.floors),
                                 state.elevator + 1,
                                 state.step + 1,
                                 state))
            state.floors[idx] -= 1

            node_count += 2  # added two nodes ...

    else:
        print("No solution found...exiting")


if __name__ == '__main__':
    solver(test_layout)
