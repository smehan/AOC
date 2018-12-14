

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


def solve(g: dict, soln=set()):
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


def solve2(g: dict, soln=set()):
    if not len(g):
        k, _ = g.popitem()
        soln.update(g[k])
        g.pop(k, None)
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


def solve3(input):
    groups = {}
    for l in input.strip().split('\n'):
        pids = {int(p) for p in l.replace(' <->', ',').split(', ')}
        pids.update(*(groups[p] for p in pids if p in groups))
        groups.update({p: pids for p in pids})
    return len(groups[0]), len({id(v) for v in groups.values()})

print(solve3(open('d12.txt', 'r').read()))

#print(solve(build_graph(test)))
#solve2(build_graph(open('d12.txt', 'r').read()))