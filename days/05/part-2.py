from parse import parse
from binary_search import binary_search

if __name__ == '__main__':

    t = parse()
    ids = []

    for boarding_pass in t:

        r = binary_search(boarding_pass[:7], 'F', 128)

        s = binary_search(boarding_pass[7:], 'L', 8)

        ids += [r * 8 + s]

    ids.sort()

    for i in range(len(ids)):
        
        if i == 0:
            continue

        if ids[i] - ids[i-1] == 2:
            print(ids[i] - 1)