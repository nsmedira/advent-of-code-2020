from sys import argv

if __name__ == "__main__":

    fin = open(argv[1])
    t = fin.read().split('\n\n')

    sum_counts = 0

    for i in t:
        temp = []
        [temp.append(j) for j in i if j not in temp and j != '\n']
        sum_counts += len(temp)

    print(sum_counts)