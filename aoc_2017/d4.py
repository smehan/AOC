"""
aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.

part ii
"""
from collections import Counter


def is_valid(phrase):
    top = (Counter(phrase.strip('\n').split(' ')).most_common(1))
    if top[0][1] > 1:
        return False
    else:
        return True

def count_valid(ps):
    count = 0
    for p in ps:
        if is_valid(p):
            count += 1
    return count

if __name__ == '__main__':
    test = ['aa bb cc dd ee',
            'aa bb cc dd aa',
            'aa bb cc dd aaa']
    with open('d4.txt', 'r') as fh:
        print(count_valid(fh.readlines()))