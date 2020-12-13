from math import *
from random import *
import time as randomTime
import pygame as pg

def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


def euclidean(point1, point2):
    return sqrt(((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2))


def randomNegative(s):
    seed(pg.time.get_ticks()*s)
    r = random()
    print(r)
    return 1 if r < 0.5 else -1