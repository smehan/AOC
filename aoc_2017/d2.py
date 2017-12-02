"""
5 1 9 5
7 5 3
2 4 6 8
The first row's largest and smallest values are 9 and 1, and their difference is 8.
The second row's largest and smallest values are 7 and 3, and their difference is 4.
The third row's difference is 6.
In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

5 9 2 8
9 4 7 3
3 8 6 5
In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
In the second row, the two numbers are 9 and 3; the result is 3.
In the third row, the result is 2.
In this example, the sum of the results would be 4 + 3 + 2 = 9.
"""


def process_file():
    out = []
    with open('d2.txt', 'r') as fh:
        body = fh.readlines()
    for l in body:
        out.append([int(n) for n in l.split('\t')])
    # return [[5,1,9,5],
    #         [7,5,3],
    #         [2,4,6,8]]
    # return [[5,9,2,8],
    #         [9,4,7,3],
    #         [3,8,6,5]]
    return out


def diff(row):
    m1, m2 = min(*row), max(*row)
    return m2 - m1


def divs(row):
    l = len(row)
    for idx in range(l):
        for j in range(l):
            if idx == j:
                continue
            if row[idx] % row[j] == 0:
                return int(row[idx] / row[j])
    return 0


def checksum(f):
    sum = 0
    for r in f:
        sum += divs(r)
    return sum


if __name__ == '__main__':
    print(checksum(process_file()))


