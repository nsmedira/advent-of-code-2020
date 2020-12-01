from parse import parse

def find_match(t):
    for number in t:
        match = 2020 - number
        if match in t: 
            return number * match
    return 'no matches found'

if __name__ == "__main__":
    print(find_match(parse()))