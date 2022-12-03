#--- Day 3: Rucksack Reorganization ---

def read_puzzle(file):
    return [item for item in open(file).read().strip().split("\n")]

def solve_1(puzzle):
    prio = 0
    for line in puzzle:
        l=int(len(line)/2)
        left = set(line[0:l])
        right = set(line[l:])
        error = left.intersection(right).pop()
        prio_error = ord(error)-ord("a") + 1 if  error.islower() else ord(error)-ord("A") + 27
        prio += prio_error
    return prio
    
def solve_2(puzzle):
    n, prio = 0, 0
    while n < len(puzzle):
        item = set(puzzle[n]).intersection(set(puzzle[n+1])).intersection(set(puzzle[n+2])).pop()
        n += 3
        prio_error = ord(item)-ord("a") + 1 if  item.islower() else ord(item)-ord("A") + 27
        prio += prio_error
    return prio

puzzle = read_puzzle('d03.txt')

print(f"Task1: {solve_1(puzzle)}")
print(f"Task2: {solve_2(puzzle)}")