# 
def read_puzzle(file):
    #x,y, 6 (6: max 6 sides)
    return [ list(map(int, (line + ",6").split(","))) for line in open(file).read().strip().split("\n")]

def count_neighbors(i, s):
    count = 0
    for item in s:
        s = 0
        for j in range(3):
            s += abs(item[j] -i[j])
        if s == 1: count+=1
    return count

def solve1(puzzle):
    for item in puzzle:
        item[3] -= count_neighbors(item, puzzle)
    return sum( item[3] for item in puzzle)

puzzle = read_puzzle('d18.txt')
print("Task 1", solve1(puzzle))
#print("Task 2", solve1(puzzle))