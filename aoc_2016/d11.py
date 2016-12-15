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
State = namedtuple('State', ['floor', 'elevator', 'step', 'parent'])


def expand(state):
    """
    expand possible nodes from current node.
    :param state:
    :return:
    """
    g = [sum(1 for v in state.floor[::2] if v == fn) for fn in range(1, 5)]
    m = [sum(1 for v in state.floor[1::2] if v == fn) for fn in range(1, 5)]
    return ''.join(map(str, g + m)) + str(state.elevator)


def is_solved(state):
    """
    checks for whether state of node is solution.
    :param state: namedtuple for present state node being checked.
    :return: True if all components on 4th floor.
    """
    return all(i == 4 for i in state.floor)


def is_valid(state):
    """
    determine if present state is a valid state.
    :param state:
    :return: True if valid, False otherwise
    """
    return True


def solver(initial_layout):
    """
    Drives for search of state-space to find solutions.
    :param initial_layout: floor for each of the components at init.
    :return:
    """
    solver_q = deque()
    # ('State', ['floor', 'elevator', 'step', 'parent'])
    solver_q.append(State(initial_layout, 1, 0, None))
    seen = set()
    node_count = 1
    while solver_q:
        state = solver_q.popleft()
        for idx in range(len(state.floor)):
            i = state.floor[idx]
            if i != state.elevator:  # skip as item not in elevator
                continue
            # first go to the floor below the present
            state.floor[idx] -= 1
            solver_q.append(State(list(state.floor),
                                 state.elevator - 1,
                                 state.step + 1,
                                 state))
            # now jump to the floor above
            state.floor[idx] += 2
            solver_q.append(State(list(state.floor),
                                 state.elevator + 1,
                                 state.step + 1,
                                 state))
            # now return to the original floor
            state.floor[idx] -= 1
            # keeping count of state nodes searched ...
            node_count += 2
            # shift index by 1 and look at adjoining component ...
            for jdx in range(idx + 1, len(state.floor)):
                # again, skip if not with elevator
                if state.floor[jdx] != state.elevator:
                    continue
                state.floor[jdx] -= 1
                state.floor[idx] -= 1
                solver_q.append(State(list(state.floor),
                                      state.elevator - 1,
                                      state.step + 1,
                                      state))
                state.floor[jdx] += 2
                state.floor[jdx] += 2
                solver_q.append(State(list(state.floor),
                                      state.elevator + 1,
                                      state.step + 1,
                                      state))
                state.floor[jdx] -= 1
                state.floor[jdx] -= 1
                node_count += 2
    else:
        print("No solution found...exiting")


if __name__ == '__main__':
    solver(test_layout)
