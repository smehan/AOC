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
        weights[node[0]] = weight_as_int(node[1])
    return weights


def weight_as_int(w: str) -> int:
    return int(w.replace('(', '').replace(')', ''))


def sieve(tree: list):
    trunk_elems = [node for node in tree if len(node) > 2]
    weights = get_weights(tree)
    remaining = deepcopy(trunk_elems)
    # this will find the one branch that doesn't appear as a child in any other branch, hence is the root
    for node in trunk_elems:
        for check in trunk_elems:
            if node == check:
                continue
            others = ' '.join(check[3:])
            if node[0] in others:
                remaining.pop(remaining.index(node))
    # assemble the trunk weights
    extended_weights = deepcopy(weights)
    for node in trunk_elems:
        extended_weights[node[0]] = weight_as_int(node[1]) + sum([int(weights[w.strip(',')]) for w in node[3:]])
        #print(node, extended_weights[node[0]], [extended_weights[n.strip(',')] for n in node[3:]])
    for node in trunk_elems:
        # if any(extended_weights[node[3].strip(',') != [extended_weights[n.strip(',')] for n in node[4:]]]):
        for n in node[4:]:
            if extended_weights[node[3].strip(',')] != extended_weights[n.strip(',')]:
                print(node, extended_weights[node[0]], [extended_weights[x.strip(',')] for x in node[3:]])

    return remaining[0][0]


print(sieve(parser(open('d7.txt').read())))
#print(sieve(parser(test)))

"""ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243
As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the other two. Even though the nodes 
above ugml are balanced, ugml itself is too heavy: it needs to be 8 units lighter for its stack to weigh 243 and keep 
the towers balanced. If this change were made, its weight would be 60."""

from collections import defaultdict, Counter

def find_root(children):
    # All nodes in the tree minus all nodes that are children.
    # N.B. sum(list of lists, []) flattens a list of lists because of how + is
    # overloaded in Python.
    root = set(children.keys()) - set(sum(children.values(),[]))
    # The root should be a single item, so we should be able to safely pop it.
    return root.pop()

def find_weight(weights, children, node, memo={}):
    # Recursively add the weight of the node to the weight of its children.
    return weights[node] + sum([find_weight(weights, children, child, memo) for
                                child in children[node]])

def find_imbalance(weights, children, node):
    # If we're at a leaf node, we can't find an imbalance.
    if not children[node]: return
    child_weights = [find_weight(weights, children, child) for child in
                     children[node]]
    weight_counts = Counter(child_weights)
    # Exit early if everything is the same.
    if len(weight_counts) <= 1: return
    # The least frequent value will be the differing value.
    # N.B. Counter.most_common() returns all counts, ordered in reverse by
    # frequency. [-1] gets the last, and [0] gets the weight.
    least_frequent_weight = weight_counts.most_common()[-1][0]
    # N.B. child_weights and children[node] are in the same order.
    lfw_node = children[node][child_weights.index(least_frequent_weight)]
    # Try to find an imbalance deeper into the tree (we want to get to the leaf
    # of the problem).
    deeper_imbalance = find_imbalance(weights, children, lfw_node)
    if deeper_imbalance:
        return deeper_imbalance
    else:
        most_frequent_weight = weight_counts.most_common(1)[0][0]
        imbalance = most_frequent_weight - least_frequent_weight
        return weights[lfw_node] + imbalance


with open('d7.txt') as inp:
    # The weight of a node.
    weights = {}
    # Adjacency list with node as the key.
    children = defaultdict(list)
    for line in inp.readlines():
        # Lines look like 'node (value) -> child1 child2 child3 ...'
        node, weight, *child_nodes = line.strip().split(' ')
        # Strip parentheses and convert an int.
        weight = int(weight.strip('()'))
        weights[node] = weight
        if child_nodes:
            # Remove the arrow ('->') and the commas after each child.
            children[node] = [child.strip(',') for child in child_nodes[1:]]

    # Part 1.
    root = find_root(children)
    print(root)

    # Part 2.
    print(find_imbalance(weights, children, root))