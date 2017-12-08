from copy import deepcopy

test = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""


def parser(input: str):
    parsed = []
    for r in input.split('\n'):
        tmp = []
        for p in r.split(' '):
            tmp.append(p)
        parsed.append(tmp)
    return parsed


def get_weights(tree: list) -> dict:
    weights = {}
    for node in tree:
        weights[node[0]] = int(node[1].replace('(', '').replace(')', ''))
    return weights


def sieve(tree: list):
    trunk_elems = [node for node in tree if len(node) > 2]
    weights = get_weights(tree)
    remaining = deepcopy(trunk_elems)
    for node in trunk_elems:
        for check in trunk_elems:
            if node == check:
                continue
            others = ' '.join(check[3:])
            if node[0] in others:
                remaining.pop(remaining.index(node))
    return remaining[0][0]


print(sieve(parser(open('d7.txt').read())))
