import sys
from os import path

def parse():

    # get path from command line argument
    try:
        arg_path = sys.argv[1]
    except IndexError:
        print("Pass the absolute path to the input file as a command line argument...")
        exit()

    # test if absolute path
    if not path.isabs(arg_path):
        print('The provided command line argument is not an absolute path...')
        exit()
    
    fin = open(arg_path)

    t = []

    for line in fin:
        t += [line.strip('\n')]

    return t

def list_strings_to_list_ints(t):
    
    for i in range(len(t)):
        t[i] = int(t[i])
    
    return t