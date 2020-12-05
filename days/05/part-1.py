from parse import parse
from binary_search import binary_search

if __name__ == '__main__':

    t = parse()

    highest_ID = -1

    for boarding_pass in t:

        r = binary_search(boarding_pass[:7], 'F', 128)

        s = binary_search(boarding_pass[7:], 'L', 8)

        id_seat = r * 8 + s

        highest_ID = max(highest_ID, id_seat)

    print(highest_ID)