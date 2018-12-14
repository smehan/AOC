"""
aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.

part ii no anagrams allowed
abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
"""
from collections import Counter


def is_unique(words):
    """pushes a list of words into a Counter and tests for no dupes in frequencies"""
    top = Counter(words).most_common(1)
    if top[0][1] > 1:
        return False
    return True


def is_valid(phrase):
    """tests for dupes in a split of words in phrase"""
    return is_unique(phrase.strip('\n').split(' '))


def no_anagram(phrase):
    """tests for anagrams of words in phrase"""
    return is_unique([''.join(sorted(w)) for w in phrase.strip('\n').split(' ')])


def count_valid(ps):
    count = 0
    for p in ps:
        if is_valid(p) and no_anagram(p):
            count += 1
    return count

# alternative using sets
import sys

def soln(pwd, hashfn):
    words = set()
    for word in pwd.split(' '):
        hashable = hashfn(word)
        if hashable in words:
            return False
        words.add(hashable)
    return True




if __name__ == '__main__':
    test = ['aa bb cc dd ee',
            'aa bb cc dd aa',
            'aa bb cc dd aaa']
    test = ['abcde fghij',
            'abcde xyz ecdab',
            'a ab abc abd abf abj',
            'iiii oiii ooii oooi oooo',
            'oiii ioii iioi iiio']
    with open('d4.txt', 'r') as fh:
        print(count_valid(fh.readlines()))

    # using sets
    result_1, result_2 = 0, 0
    identity = lambda x : x
    counter_hash = lambda x: frozenset(Counter(x).items())
    for line in sys.stdin:
        result_1 += soln(line.strip(), identity)
        result_2 += soln(line.strip(), counter_hash)

    print('Part 1: {}, Part 2: {}'.format(result_1, result_2))

    """
    from collections import Counter

def solve(input, fn):
    phrases = [Counter(fn(p)) for p in input.strip().split('\n')]
    return sum(1 for p in phrases if p.most_common(1)[0][1] == 1)

solve(input, lambda p: p.split())  # Part 1
solve(input, lambda p: (''.join(sorted(w)) for w in p.split()))  # Part 2
"""