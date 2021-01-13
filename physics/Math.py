from math import *
from random import *
import math
import pygame as pg


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


def euclidean(point1, point2):
    return sqrt(((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2))


def randomNegative(s):
    seed(pg.time.get_ticks() * s)
    r = random()
    # print(r)
    return 1 if r < 0.5 else -1


def positionWithin(check, static):
    if static[0] < check[0] < static[0] + static[2] and static[1] < check[1] < static[1] + static[3]:
        return True
    return False


def randomAngle(vector, angle):
    seed(pg.time.get_ticks())
    r = random()
    angle = randrange(0, round(angle / 2)) * (1 if r < 0.5 else -1)

    return rotateVector(vector, angle)


def rotateVector(vector, angle):
    x = math.cos(radians(angle)) * vector[0] - math.sin(radians(angle)) * vector[1]
    y = (math.sin(radians(angle)) * vector[0]) + (math.cos(radians(angle)) * vector[1])

    return x, y


def subTuples(t1, t2):
    return t1[0]-t2[0], t1[1]-t2[1]


def sumTuples(t1, t2):
    return t1[0]+t2[0], t1[1]+t2[1]


def angleBetweenVectors(vector1, vector2):
    angle = math.degrees(math.acos(dot(vector1, vector2)))
    vector2 = rotateVector(vector2, 90)
    direction = vector1[0] * vector2[0] - vector1[1] * vector2[1]
    if direction < 0:
        return angle*-1
    else:
        return angle


def dot(vector1, vector2):
    return vector1[0] * vector2[0] + vector1[1] * vector2[1]
