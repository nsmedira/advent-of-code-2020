from parse import parse

def find_three(t):

    # sort ascending
    t.sort()

    for i in range(len(t)):
        for j in range(i+1, len(t)):
            match = 2020 - t[i] - t[j]
            if match < 0:
                break
            if match in t:
                return t[i] * t[j] * match
    return 'no match found'

if __name__ == "__main__":
    print(find_three(parse()))