from parse import parse
from papers import valid_passport, count_passports

if __name__ == "__main__":

    t = parse()

    print(count_passports(t, valid_passport))