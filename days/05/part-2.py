from parse import parse
from binary_search import get_row_and_seat

if __name__ == '__main__':

    t = parse()
    ids = []

    for boarding_pass in t:

        r, s = get_row_and_seat(boarding_pass)

        ids += [r * 8 + s]

    ids.sort()

    for i in range(len(ids)):

        if i == 0:
            continue

        if ids[i] - ids[i-1] == 2:
            print(ids[i] - 1)