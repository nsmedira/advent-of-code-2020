from parse import parse
from split_n_strip import *

if __name__ == "__main__":

    t = parse()

    number_valid = 0

    # convert each entry in the list into a list
    for i in range(len(t)):

        u = split_n_strip(t[i])

        # does it fit policy?
        letter = u[1]
        a = u[2][int(u[0][0]) - 1]
        b = u[2][int(u[0][1]) - 1]
        if (
            (
                a == letter
                or b == letter
            )
            and a != b
            
        ):
            number_valid += 1

    print(number_valid)