#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full

    res = [[0 for i in range(capacity + 1)] for j in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        cw = items[i - 1].weight
        cv = items[i - 1].value

        for j in range(0, capacity + 1):

            if cw > j:
                res[i][j] = res[i - 1][j]
            else:
                res[i][j] = max(res[i - 1][j], cv + res[i - 1][j - cw])

    value = res[-1][-1]
    taken = getKnapsackValues(res, items)                

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


def getKnapsackValues(res, items):
    i = len(res) - 1 
    c = len(res[0]) - 1
    sequence = [0] * len(items);

    while i > 0:

        if res[i][c] == res[i - 1][c]:
            i -= 1
        else:
            sequence[items[i - 1].index] = 1
            c -= items[i - 1].weight
            i -= 1

        if c == 0:
            break        

    return sequence        

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

