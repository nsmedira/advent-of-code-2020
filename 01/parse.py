def parse():
    fin = open('input.txt')

    numbers = []

    for entry in fin:
        numbers += [int(entry.strip('\n'))]

    return numbers