###########################################################
# Copyright (C) 2015-2016 Shawn Mehan <shawn dot mehan at shawnmehan dot com>
# day 11 of AOC_2016
###########################################################
#
#  -*- coding: utf-8 -*-

# standard libs
from collections import deque, namedtuple
import time

# 3rd party libs
import numpy as np

# application libs

########################
# initialization
########################

test_components = ['HG', 'HM', 'LiG', 'LiM']
test_layout = [2, 1, 3, 1]

components = ['prg', 'prm', 'cog', 'com', 'rug', 'rum', 'plg', 'plm', 'cug', 'cum']
layout = [1, 1, 2, 3, 2, 3, 2, 3, 2, 3]

components_2 = components + ['elg', 'elm', 'dig', 'dim']
layout_2 = layout + [1, 1, 1, 1]

State = namedtuple('State', ['floor', 'elevator', 'step', 'parent'])


def summarize(state):
    """
    Represents how many generators and microchips are on each floor.

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
    if not 1 <= state.elevator <= 4:
        return False
    if any(not 1 <= i <= 4 for i in state.floor):
        return False

    for idx, v in enumerate(state.floor[1::2]):
        idx = idx * 2 + 1
        if v != state.floor[idx - 1] and any(v == i for i in state.floor[0::2]):
            return False

    return True


def draw_state(s, names):
    """
    Draw present state onto screen.
    :param s:
    :param names: names to use for animation
    :return:
    """
    print('\x1b[2J\x1b[H', end="")
    for floor in range(4, -1, -1):
        out = 'F{}: '.format(floor)
        out += ' '.join(names[idx] if i == floor else '   ' for idx, i in enumerate(s.floor))
        if floor == s.elevator:
            out += ' [E]'
        print(out)
    time.sleep(0.4)


def animate(state, version):
    """
    drives an ascii animation of state space search.
    :param state:
    :param version: which components list to use for animation
    :return:
    """
    parents = []

    if version == 't':
        names = test_components
    elif version == '1':
        names = components
    else:
        names = components_2
    while state:
        parents.append(state)
        state = state.parent
    parents.reverse()
    for p in parents:
        draw_state(p, names)
    print('*'*15 + '\n')


def solver(initial_layout, version='1'):
    """
    Drives for search of state-space to find solutions.
    :param initial_layout: floor for each of the components at init.
    :param version: three choices of version: t: test, 1: part 1, 2: part 2
    :return:
    """
    solver_q = deque()
    # ('State', ['floor', 'elevator', 'step', 'parent'])
    solver_q.append(State(initial_layout, 1, 0, None))
    seen = set()
    node_count = 1

    while solver_q:
        state = solver_q.popleft()
        if summarize(state) in seen or not is_valid(state):
            continue
        seen.add(summarize(state))

        # check to see if reached target state and exit
        if is_solved(state):
            animate(state, version)
            print('Search of version {} space complete.'.format(version))
            print('Solution found in {} steps.'.format(state.step))
            print('{} state nodes searched ....'.format(node_count))
            return

        # not solved so continue to search state-space
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

            # shift index by 1 and permute adjoining component ...
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
                state.floor[idx] += 2
                solver_q.append(State(list(state.floor),
                                      state.elevator + 1,
                                      state.step + 1,
                                      state))
                state.floor[jdx] -= 1
                state.floor[idx] -= 1
                node_count += 2
    else:
        print("No solution found...exiting")


if __name__ == '__main__':
    solver(layout_2, version='2')
