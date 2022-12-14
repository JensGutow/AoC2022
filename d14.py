#  --- Day 14: Regolith Reservoir ---
import copy
from pygame.math import Vector2 as V

def read_puzzle(file):
    paths =   [[V([int(point) for point in path.split(",")]) for path in line.split(" -> ")]   for line in open(file).read().strip().split("\n")]
    points = [point for path in paths for point in path] 
    max_y = int(max(p[1] for p in points))
    min_x = int(min(p[0] for p in points))
    max_x = int(max(p[0] for p in points))
    cave = {}
    for path in paths:
        for i2, p1 in enumerate(path[:-1], 1):
            p2 = path[i2]
            dx, dy = p2 - p1
            if dx : dx = dx//abs(dx)
            if dy : dy = dy//abs(dy)
            dP = V(dx, dy)
            while True:
                cave[tuple(p1)] = "#"
                if p1 == p2:
                    break
                p1 = p1 + dP
    return max_y, min_x, max_x, cave

def cave_simu_step(src, max_y, cave, steps):
    item = src
    if tuple(item) in cave: return False

    finish = False
    while not finish:
        checks = [V(0,1), V(-1,1), V(1,1)]
        finish = True
        for check in checks:
            check_pos = item + check
            if tuple(check_pos) not in cave:
                if check_pos[1] > max_y: 
                    return False
                else: 
                    item = check_pos
                    finish = False
                    break    
    cave[tuple(item)] = "O"
    steps[0] += 1
    return True

def solve1(puzzle):
    max_y, min_x, max_x, cave = puzzle
    cave2 = copy.deepcopy(cave)
    START = V(500,0)
    s1 = [0]
    while cave_simu_step(START, max_y, cave, s1): pass

    y = max_y+2
    for x in range(min_x-3-max_y, max_x +4 + max_y):
        cave2[(x,y)] = "#"
    s2 = [0]
    while cave_simu_step(START, max_y+3, cave2, s2): pass

    return s1[0], s2[0]

puzzle = read_puzzle('d14.txt')

print("Task 1/2", solve1(puzzle))