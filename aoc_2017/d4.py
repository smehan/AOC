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


def is_valid(phrase):
    top = (Counter(phrase.strip('\n').split(' ')).most_common(1))
    if top[0][1] > 1:
        return False
    else:
        return True


def no_anagram(phrase):
    words = [''.join(sorted(w)) for w in phrase.strip('\n').split(' ')]
    top = Counter(words).most_common(1)
    if top[0][1] > 1:
        return False
    return True


def count_valid(ps):
    count = 0
    for p in ps:
        if is_valid(p) and no_anagram(p):
            count += 1
    return count


if __name__ == '__main__':
    test = ['aa bb cc dd ee',
            'aa bb cc dd aa',
            'aa bb cc dd aaa']
    test = ['abcde fghij',
            'abcde xyz ecdab',
            'a ab abc abd abf abj',
            'iiii oiii ooii oooi oooo',
            'oiii ioii iioi iiio']
    print(count_valid(test))
    with open('d4.txt', 'r') as fh:
        print(count_valid(fh.readlines()))