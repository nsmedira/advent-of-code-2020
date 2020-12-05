from parse import parse
from papers import is_passport, count_passports

if __name__ == "__main__":

    t = parse()

    print(count_passports(t, is_passport))