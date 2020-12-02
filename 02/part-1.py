from parse import parse
from split_n_strip import *

if __name__ == "__main__":

    t = parse()
    
    number_valid = 0

    # convert each entry in the list into a list
    for i in range(len(t)):

        u = split_n_strip(t[i])

        # count how many times the letter appears
        count = 0
        for j in list(u[2]):
            if j == u[1]:
                count += 1
        
        # does it fit policy?
        if count >= int(u[0][0]) and count <= int(u[0][1]):
            number_valid += 1

    print(number_valid)