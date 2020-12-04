from parse import parse
from bomb_the_slope import *
from math import prod

if __name__ == "__main__":

    t = parse()

    print(
        prod([
            bomb_the_slope(t, 1, 1),
            bomb_the_slope(t, 3, 1),
            bomb_the_slope(t, 5, 1),
            bomb_the_slope(t, 7, 1),
            bomb_the_slope(t, 1, 2)
        ])
    )