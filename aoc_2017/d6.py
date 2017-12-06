"""
In this area, there are sixteen memory banks; each memory bank can hold any number of blocks. The goal of the
reallocation routine is to balance the blocks between the memory banks.

The reallocation routine operates in cycles. In each cycle, it finds the memory bank with the most blocks
(ties won by the lowest-numbered memory bank) and redistributes those blocks among the banks. To do this,
it removes all of the blocks from the selected bank, then moves to the next (by index) memory bank and inserts
one of the blocks. It continues doing this until it runs out of blocks; if it reaches the last memory bank, it wraps around to the first one.

The debugger would like to know how many redistributions can be done before a blocks-in-banks configuration
is produced that has been seen before.

For example, imagine a scenario with only four memory banks:

The banks start with 0, 2, 7, and 0 blocks. The third bank has the most blocks, so it is chosen for redistribution.
Starting with the next bank (the fourth bank) and then continuing to the first bank, the second bank, and so on,
the 7 blocks are spread out over the memory banks. The fourth, first, and second banks get two blocks each,
and the third bank gets one back. The final result looks like this: 2 4 1 2.

Next, the second bank is chosen because it contains the most blocks (four). Because there are four
memory banks, each gets one block. The result is: 3 1 2 3.
Now, there is a tie between the first and fourth memory banks, both of which have three blocks. The first
bank wins the tie, and its three blocks are distributed evenly over the other three banks, leaving it with none: 0 2 3 4.
The fourth bank is chosen, and its four blocks are distributed such that each of the four banks receives one: 1 3 4 1.
The third bank is chosen, and the same thing happens: 2 4 1 2.

At this point, we've reached a state we've seen before: 2 4 1 2 was already seen. The infinite loop is
detected after the fifth block redistribution cycle, and so the answer in this example is 5.

Given the initial block counts in your puzzle input, how many redistribution cycles must be completed before a configuration is produced that has been seen before?
"""
import time
from collections import deque


def redistribute(state: list):
    biggest = max(state)
    big_index = state.index(biggest)
    state[big_index] = 0
    while biggest:
        big_index = (big_index + 1) % len(state)
        state[big_index] += 1
        biggest -= 1
    return state


def is_solved(s: deque, goal: list, limit=1):
    if s.count(goal) > limit:
        return True
    return False


def solve(s: deque):
    new = redistribute(s[0][:])
    while not is_solved(s, new):
        new = redistribute(new[:])
        s.appendleft(new)
    print(len(s))
    first_loop = len(s)
    print(s[0])
    while not is_solved(s, new, 2):
        print(f'\r{new}', end='', flush=True)
        time.sleep(0.1)
        new = redistribute(new[:])
        s.appendleft(new)
    return len(s)-first_loop


states = deque()
#states.appendleft([0,2,7,0])
states.appendleft([2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14])
print(f'\n{solve(states)}')


