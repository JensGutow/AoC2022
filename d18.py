# 
def read_puzzle(file):
    #x,y, 6 (6: max 6 sides)
    return [ list(map(int, (line).split(","))) for line in open(file).read().strip().split("\n")]

def blowUp(LavaDroplet, minx, maxx, miny, maxy, minz, maxz):
    item = (minx, miny, minz)
    openSet = set()
    openSet.add(item)
    closedSet = set()
    n_borders_to_LavaDroplet = 0
    while openSet:
        item = openSet.pop()
        for dir_ in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
            nextItem =  tuple(i+d for i,d in zip(item, dir_))
            if nextItem in closedSet: continue
            if nextItem in openSet : continue
            if list(nextItem) in LavaDroplet: 
                n_borders_to_LavaDroplet +=1
                continue
            if minx > nextItem[0] or maxx < nextItem[0] or miny > nextItem[1] or maxy < nextItem[1] or minz > nextItem[2] or maxz < nextItem[2]:
                continue
            openSet.add(nextItem)
        closedSet.add(item)
    return n_borders_to_LavaDroplet

def count_neighbors(i, s):
    count = 0
    for item in s:
        s = 0
        for j in range(3):
            s += abs(item[j] -i[j])
        if s == 1: count+=1
    return count

def solve1(puzzle):
    nb = []
    for item in puzzle:
        nb.append(6 - count_neighbors(item, puzzle))
    n_task1 =  sum(nb)

    minx = min([i[0] for i in puzzle])
    maxx = max([i[0] for i in puzzle])
    miny = min([i[1] for i in puzzle])
    maxy = max([i[1] for i in puzzle])
    minz = min([i[2] for i in puzzle])
    maxz = max([i[2] for i in puzzle])
    
    n = blowUp(puzzle, minx-1, maxx+1, miny-1, maxy+1, minz-1, maxz+1)
    
    return n_task1,  n

puzzle = read_puzzle('d18.txt')
print("Task 1+2:", solve1(puzzle))