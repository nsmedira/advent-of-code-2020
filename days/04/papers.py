def is_passport(d):

    return (
        'byr' in d
        and 'iyr' in d
        and 'eyr' in d
        and 'hgt' in d
        and 'hcl' in d
        and 'ecl' in d
        and 'pid' in d
    )

def get_digits_from_string(string):

    return ''.join(filter(str.isdigit, string))

def valid_passport(d):

    if not is_passport(d):
        return False

    byr = d.get('byr')
    iyr = d.get('iyr')
    eyr = d.get('eyr')
    hgt = d.get('hgt')
    hcl = d.get('hcl')
    ecl = d.get('ecl')
    pid = d.get('pid')

    hgt_number = get_digits_from_string(hgt)
    len_hgt = len(hgt_number)
    hgt_number = int(hgt_number)
    hgt_unit = hgt[len_hgt:]
    if hgt_unit == 'cm':
        hgt_valid = hgt_number >= 150 and hgt_number <= 193
    elif hgt_unit == 'in':
        hgt_valid = hgt_number >= 59 and hgt_number <= 76
    else:
        hgt_valid = False

    if len(hcl) != 7:
        hcl_valid = False
    else:
        hcl_valid = hcl[0] == '#'

    ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    return (
        len(byr) == 4 and int(byr) >= 1920 and int(byr) <= 2002
        and len(iyr) == 4 and int(iyr) >= 2010 and int(iyr) <= 2020
        and len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030
        and hgt_valid
        and hcl_valid 
        and ecl in ecls
        and len(pid) == 9 and len(get_digits_from_string(pid)) == 9
    )

def count_passports(t, f):

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

            if f(temp):
                valid += 1

            temp = dict()

            continue

    return valid