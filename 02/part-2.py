from parse import parse

if __name__ == "__main__":

    t = parse()

    number_valid = 0

    # convert each entry in the list into a list
    for i in range(len(t)):

        t[i] = t[i].split()

        # t[i][0] will now be the range. split with '-'
        # t[i][1] will be the character. strip ':'
        # leave t[i][2] unmodified
        t[i] = [t[i][0].split('-'), t[i][1].strip(':'), t[i][2]]
        
        # does it fit policy?
        letter = t[i][1]
        a = t[i][2][int(t[i][0][0]) - 1]
        b = t[i][2][int(t[i][0][1]) - 1]
        if (
            (
                a == letter
                or b == letter
            )
            and a != b
            
        ):
            number_valid += 1

    print(number_valid)