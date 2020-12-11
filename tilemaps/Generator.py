import os
from random import *

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) + "\\"


def randomizeGrass():
    tilemap = input()
    seed(tilemap)
    generatedMap = []

    with open(__location__ + tilemap, "rt") as f:
        for row, line in enumerate(f):

            new_line = []
            for column, tile in enumerate(line):
                if tile == ".":
                    if random() > 0.5:
                        new_line.append(".")
                    else:
                        new_line.append(":")
                else:
                    new_line.append(tile)

            generatedMap.append(new_line)

    with open(__location__ + "generated\\" + tilemap, "w") as f:
        for row in generatedMap:
            for col in row:
                f.write(col)


randomizeGrass()
