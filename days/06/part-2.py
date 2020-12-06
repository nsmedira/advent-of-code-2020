from sys import argv

if __name__ == "__main__":

    t = [list(x.split()) for x in open('input.txt').read().split('\n\n')]

    sum_counts = 0

    for i in t:

        temp = dict()

        for j in i:
            for k in j:                
                temp[k] = temp.setdefault(k, 0) + 1

        count = 0 
        for key in temp:
            if temp[key] == len(i):
                count += 1

        sum_counts += count

    print(sum_counts)