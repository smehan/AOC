###########################################################
# Copyright (C) 2015-2016 Shawn Mehan <shawn dot mehan at shawnmehan dot com>
# day 1 of AOC_2016
###########################################################
#
#  -*- coding: utf-8 -*-

# standard libs
import copy

# 3rd party libs
import numpy as np

# application libs


directions = """R1, R3, L2, L5, L2, L1, R3, L4, R2, L2, L4, R2, L1, R1, L2, R3, L1, L4, R2, L5, R3, R4, L1, R2, L1, R3, L4, R5, L4, L5, R5, L3, R2, L3, L3, R1, R3, L4, R2, R5, L4, R1, L1, L1, R5, L2, R1, L2, R188, L5, L3, R5, R1, L2, L4, R3, R5, L3, R3, R45, L4, R4, R72, R2, R3, L1, R1, L1, L1, R192, L1, L1, L1, L4, R1, L2, L5, L3, R5, L3, R3, L4, L3, R1, R4, L2, R2, R3, L5, R3, L1, R1, R4, L2, L3, R1, R3, L4, L3, L4, L2, L2, R1, R3, L5, L1, R4, R2, L4, L1, R3, R3, R1, L5, L2, R4, R4, R2, R1, R5, R5, L4, L1, R5, R3, R4, R5, R3, L1, L2, L4, R1, R4, R5, L2, L3, R4, L4, R2, L2, L4, L2, R5, R1, R4, R3, R5, L4, L4, L5, L5, R3, R4, L1, L3, R2, L2, R1, L3, L5, R5, R5, R3, L4, L2, R4, R5, R1, R4, L3"""


class Walker(object):
    """
    takes an input string and computes the path taken, the distance
    from the origin (0,0j) and the crossing points on the path.
    """

    def __init__(self):
        self.pos = 0 + 0j
        self.bearing = 0 + 1j
        self.points = [(0 + 0j)]  # history of all points in path

    @staticmethod
    def make_path(directions):
        """take an input string of directions and
        construct a path with components as elements of
        a list
        :param directions: string of directions to turn and move, e.g. R2, L3
        :return: list of elements"""
        return directions.split(',')

    def update_points(self, segment):
        """accepts a segment from input and computes next step
        with updates to bearing. updates points
        :param segment: string representing direction to turn and distance to walk in complete blocks
        :return:
        """
        if 'R' in segment:
            self.bearing *= -1j
        else:
            self.bearing *= 1j
        segment = int(segment.strip()[1:]) * self.bearing
        self.pos += segment
        self.points.append(self.pos)
        # print("\nBearing changed to {}".format(self.bearing))
        # print("Now at {}".format(self.pos))
        # print("Total distance is {}".format(self.pos.real + self.pos.imag))

    @staticmethod
    def is_parallel(A, B, C, D):
        """if same x, or y component remains constant, is parallel"""
        AB_x = (B.real - A.real)
        AB_y = (B.imag - A.imag)
        CD_x = (D.real - C.real)
        CD_y = (D.imag - C.imag)
        if AB_x == CD_x or AB_y == CD_y:
            return True
        else:
            return False

    @staticmethod
    def in_between(a, b, c):
        """checks if c in (a, b)
        :param a: number
        :param b: number
        :param c: number
        return: True if c in interval, False otherwise
        """
        if a > b > c or a < b < c:
            return True
        else:
            return False

    def find_crosses(self, A, B, C, D):
        """AB and CD are perpendicular segments. Determine if
        two segments cross. Endpoints are (real, imag) in C.
        :param A: endpoint of segment AB
        :param B: endpoint of segment AB
        :param C: endpoint of segment CD
        :param D: endpoint of segment CD
        return:
        """
        CD_x = abs(D.real - C.real)
        CD_y = abs(D.imag - C.imag)
        if self.in_between(A.real, C.real, B.real) and self.in_between(C.imag, A.imag, D.imag):
            if CD_x == 0:
                dir = 'x'
                distance = abs(C.real) + abs(A.imag)
            elif CD_y == 0:
                dir = 'y'
                distance = abs(C.imag) + abs(A.real)
            print("CD intersects AB in {}".format(dir))
            print("Cross {}, {} with {}, {}".format(C, D, A, B))
            print("Distance to origin is {}".format(distance))


if __name__ == '__main__':
    bunny = Walker()
    for e in bunny.make_path(directions):
        bunny.update_points(e)
    stack = copy.copy(bunny.points)
    stack = stack[1:]
    for idx, p in enumerate(stack):
        if idx + 1 < len(stack):
            for oidx, op in enumerate(bunny.points):
                if oidx <= idx:
                    if bunny.is_parallel(bunny.points[oidx], bunny.points[oidx + 1], stack[idx], stack[idx+1]):
                        continue
                    bunny.find_crosses(bunny.points[oidx], bunny.points[oidx + 1], stack[idx], stack[idx + 1])

