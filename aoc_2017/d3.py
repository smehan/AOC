"""
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
(2n+1)^2
mids for 2nd: 2,4,6,8
mids for 3rd: 11,15,19,23
mids for 4th: 28,34, ,46
n^2+(n-1)
"""


def steps_from_origin(p, s=1):
    """tells us which increasing square of grid a point lies in"""
    if p == 1:
        return 1
    elif p > (2*s+1)**2:
        s += 1
        return steps_from_origin(p, s)
    else:
        return s


def distance_midpoint(p, n):
    """each side is 2n-1 """
    # special case of center of grid
    if n == 1:
        return n
    side = (2*n+1)
    start = side**2
    values = []
    for i in range(1,4,1):
        top = start-side*(i-1)
        bottom = top - side
        values = list(range(top, bottom, -1))
        if p in values:
            mid = values[round(len(values)/2)]
            return mid-p+n

def man_distance(p):
    ...


def manhattan_distance(start, end):
    sx, sy = start
    ex, ey = end
    return abs(ex - sx) + abs(ey - sy)


def part_2(p):
    total, level = 1, 1

    while total < p:
        level += 2
        total = total + level * 4 - 4  # or the easy (not my) way: total = level ** 2

    offset = total - p
    steps = offset % (level - 1)

    print((level - 1) / 2 + abs((level / 2) - steps))

    # x, y, value
    values = [(0, 0, 1)]

    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    level = 1
    x, y = 0, 0

    terminate = False

    while not terminate:

        for direction in range(4):

            if terminate:
                break

            dirX, dirY = directions[direction]

            if direction == 0:
                moveN = level - 2
            elif direction in [1, 2]:
                moveN = level - 1
            else:
                moveN = level

            for _ in range(moveN):

                x += dirX
                y += dirY

                new = sum([k[2] for k in values if abs(x - k[0]) <= 1 and abs(y - k[1]) <= 1])
                values.append((x, y, new))

                if new >= p:
                    print
                    new

                    terminate = True
                    break

        level += 2

if __name__ == '__main__':
    test = [1,12,23,1024]
    data = [368078]
    for t in data:
        print(distance_midpoint(t,steps_from_origin(t)), steps_from_origin(t))
        part_2(t)