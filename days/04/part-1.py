from parse import parse

def validate_passport(d):

    print(d)

    return (
        'byr' in d
        and 'iyr' in d
        and 'eyr' in d
        and 'hgt' in d
        and 'hcl' in d
        and 'ecl' in d
        and 'pid' in d
    )

if __name__ == "__main__":

    t = parse()

    temp = dict()
    valid = 0
    length = len(t)

    for i in range(length):

        if t[i] != '':

            split = t[i].split()

            for field in split:
                pair = field.split(':')
                temp[pair[0]] = pair[1]

        if t[i] == '' or i == length - 1:

            if validate_passport(temp):
                valid += 1

            temp = dict()

            continue

    print(valid)