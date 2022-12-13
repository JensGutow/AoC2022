# --- Day 13: Distress Signal ---
import copy
from functools import cmp_to_key

def read_puzzle(file):
    return [[eval(x) for x in line.split("\n")] for line in open(file).read().strip().split("\n\n")]

def compare(a, b): # (result, fuzzy) : fuzzy == True -> compare_result is unknown, else: compare_result = result
    aIsList = isinstance(a, list)
    bIsList = isinstance(b, list)
    if not aIsList and not bIsList : return (a < b, a == b)
    elif aIsList != bIsList:
        if not aIsList: a = [a]
        if not bIsList: b = [b]
        return compare(a,b)
    else:
        for az, bz in zip(a, b):
            result, isUndef = compare(az, bz)
            if not isUndef: return result, False
        return len(a) < len(b), len(a) == len(b)

def comp(a, b):
    return compare(a, b)[0]

def solve1(puzzle):
    return sum([(i + 1) * compare(item[0], item[1])[0] for i, item in enumerate(puzzle)])

def solve2(puzzle):
    p = []
    for items in puzzle:
        a, b = items
        p.append(a)
        p.append(b)

    addList = [[2], [6]]
    p.append(addList[0])
    p.append(addList[1])
    
    p.sort(key = cmp_to_key(comp))

    # sorted = []
    # while p:
    #     item = copy.deepcopy(p[0])
    #     next = copy.deepcopy(item)
    #     for next in p[1:]:
    #             item = copy.deepcopy(item) if compare(item, next)[0] else copy.deepcopy(next)
    #     p.pop(p.index(item))
    #     sorted.append(item)

    i1 = p.index(addList[0]) + 1
    i2 = p.index(addList[1]) + 1

    return i1 * i2

puzzle = read_puzzle('d13.txt')
print("Task 1", solve1(puzzle))
print("Task 2", solve2(puzzle))
