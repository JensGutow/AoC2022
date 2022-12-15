# --- Day 15: Beacon Exclusion Zone ---
import re

def read_puzzle(file):
    return [list(map(int,re.findall(r"[-]?[\d]+", line))) for line in  open(file).read().split("\n")]

def check_high(y, puzzle):
    y_set = set()
    b_set = set() 
    for sx,sy, bx, by in puzzle:
        d_sensor_bacon = abs(bx-sx) + abs(by-sy)
        d_sensor_y = abs(y-sy)
        if by == y: b_set.add(bx)
        n = d_sensor_bacon - d_sensor_y
        if n > 0:
            for x in range(n+1):
                y_set.add(sx + x)
                y_set.add(sx - x)
    y_set = y_set - b_set
    return y_set

def get_borderSet(x,y,r):
    bs = set()
    px = x
    py = y-r
    for dx, dy in[[1,1], [-1,1], [-1,-1], [1,-1]]:
        for _ in range(r):
            bs.add((px, py))
            px += dx
            py += dy
    return bs

def solve1(puzzle, test):
    y = 10 if test else 2000000
    # part 1
    y_set = check_high(y, puzzle)
    return len(y_set)


def solve2(puzzle, test):
    # checker area
    ymin = xmin = 0
    ymax = xmax = 20 if test else 4000000

    borderSet = set()
    # gather the border sets of all circles (inside the checker area)
    print("gather the border sets of")
    for i, (sx,sy, bx, by) in enumerate(puzzle):
        print("start ",i, "form ", len(puzzle))
        r = abs(bx-sx) + abs(by-sy)
        bs = get_borderSet(sx, sy, r+1)
        bs = {p for p in bs if (xmin <= p[0] <= xmax) and (ymin <= p[1] <= ymax)}
        borderSet = borderSet.union(bs)

    # exclude all items in borderset - if a item is in a SensorCircle to its nearest bacon
    print("Excude Step")
    for i, (sx,sy, bx, by) in enumerate(puzzle):
        print("start ",i, "from ", len(puzzle))
        r = abs(bx-sx) + abs(by-sy)
        borderSet = {p for p in borderSet if ((abs(p[0]-sx) + abs(p[1]-sy)) > r) }
    
    p = borderSet.pop()
    
    return 4000000*p[0] + p[1]

puzzle = read_puzzle('d15.txt')

test = False
print("Task 1", solve1(puzzle, test))
print("Task 2", solve2(puzzle, test))