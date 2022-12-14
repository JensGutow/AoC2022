#  --- Day 14: Regolith Reservoir ---
import copy

def read_puzzle(file):
    paths =   [[[int(coord) for coord in path.split(",")] for path in line.split(" -> ") ] for line in open(file).read().strip().split("\n") ]
    max_y = max([coords[1] for path in paths for coords in path])
    x = ([coords[0] for path in paths for coords in path])
    min_x = min(x)
    max_x = max(x)
    grave = {}
    for path in paths:
        for i2, p1 in enumerate(path[:-1], 1):
            p2 = path[i2]
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            if dx : dx = dx//abs(dx)
            if dy : dy = dy//abs(dy)
            x = p1[0]
            y = p1[1]
            while True:
                grave[(x,y)] = "#"
                if x == p2[0] and y == p2[1]:
                    break
                x += dx
                y += dy
    return max_y, min_x, max_x, grave

def grave_simu_step(src, max_y, min_x, max_x, grave):
    item = src
    if tuple(item) in grave: return False

    finish = False
    while not finish:
        checks = [(0,1), (-1,1), (1,1)]
        finish = True
        for check in checks:
            check_pos = [item[0] + check[0], item[1] + check[1]]
            if tuple(check_pos) not in grave:
                if check_pos[1] > max_y: 
                    return False
                else: 
                    item = check_pos
                    finish = False
                    break    
    grave[tuple(item)] = "O"
    return True


def solve1(puzzle):
    max_y, min_x, max_x, grave = puzzle
    grave2 = copy.deepcopy(grave)
    SRC = [500,0]
    i = True
    while i: 
        i = grave_simu_step(SRC, max_y, min_x, max_x, grave)
    s1 = sum( [1 for v in grave.values() if v=="O"])

    y = max_y+2
    for x in range(min_x-3-max_y, max_x +4 + max_y):
        grave2[(x,y)] = "#"
    test = True
    while test: 
        test = grave_simu_step(SRC, max_y+3, min_x, max_x, grave2)
    s2 = sum( [1 for v in grave2.values() if v=="O"])

    return s1, s2

puzzle = read_puzzle('d14.txt')

print("Task 1/2", solve1(puzzle))