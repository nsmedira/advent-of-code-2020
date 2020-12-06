from math import floor, ceil

def binary_search(string, specify_lower, length):

    r = [0, length - 1]

    for i in string:

        dif = (r[1] - r[0]) / 2
        if i == specify_lower:
            r = [r[0], r[0] + floor(dif)]
        else:
            r = [r[0] + ceil(dif), r[1]]

    return r[0]

def get_row_and_seat(string):

    return binary_search(string[:7], 'F', 128), binary_search(string[7:], 'L', 8)