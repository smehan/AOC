

test = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""


def build_graph(input, graph = {}):
    for row in input.splitlines():
        base, _, targets = row.split(' ', 2)
        graph[base] = targets.split(', ')
    return graph


def solve(g: dict, soln = set()):
    if g.get('0', None):
        soln.update(g['0'])
        g.pop('0', None)
        # if base == 0:
        #     soln.append(targets.split(', '))
        # elif
    for e in list(soln):
        if e in g.keys():
            soln.update((map((lambda x: x), (g.get(e)))))
            g.pop(e, None)
    if set(g.keys()).intersection(soln):
        g, soln = solve(g, soln)
    else:
        return g, soln

    print(g)
    print(len(soln))
    print(len([v for k, v in g.items() if k != '0']))


#print(solve(build_graph(test)))
print(solve(build_graph(open('d12.txt', 'r').read())))