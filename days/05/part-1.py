from parse import parse
from binary_search import get_row_and_seat

if __name__ == '__main__':

    t = parse()

    highest_ID = -1

    for boarding_pass in t:

        r, s = get_row_and_seat(boarding_pass)

        id_seat = r * 8 + s

        highest_ID = max(highest_ID, id_seat)

    print(highest_ID)