# --- Day 13: Distress Signal ---
import copy

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
        for az,bz in zip(a, b):
            result, isUndef = compare(az, bz)
            if not isUndef: return result, False
        return len(a) < len(b), len(a) == len(b)

def solve1(puzzle):
    return sum([(i + 1) * compare(a, b)[0] for i, a, b in enumarate(puzzle)])

def solve2(puzzle):
    p = [ *p for p in puzzle]
    addList = [[2], [6]]
    for l in addList:
        p.append(l)

    sorted = []

    while p:
        item = copy.deepcopy(p[0])
        next = copy.deepcopy(item)
        for next in p[1:]:
                item = copy.deepcopy(item) if compare(item, next)[0] else copy.deepcopy(next)
        p.pop(p.index(item))
        sorted.append(item)

    i1 = sorted.index(addList[0]) + 1
    i2 = sorted.index(addList[1]) + 1

    return i1 * i2

puzzle = read_puzzle('d13.txt')

print("Task 1", solve1(puzzle))
print("Task 2", solve2(puzzle))
