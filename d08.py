# --- Day 8: Treetop Tree House ---

from collections import defaultdict
import numpy as np

class Vector():
    def __init__(self, x,y) -> None:
        self.x = x
        self.y = y 

    def add(self, v):
        self.x += v.x
        self.y += v.y

    def copy(self):
        return Vector(self.x, self.y)

    def __repr__(self) -> str:
        return f"Point: x={self.x}, y={self.y}"

class Tree():
    def __init__(self, c) -> None:
        self.high = int(c)
        self.visible = False
        self.score = defaultdict() # dir:score


    def __repr__(self) -> str:
        return f"({self.high}, {self.visible} {self.score})"

def read_puzzle(file):
    return [[Tree(c) for c in line] for line in open(file).read().split("\n")]

def solve1(puzzle):
    assert len(puzzle) == len(puzzle[1])
    # part 1
    #       start_point, checking_direction, offet_next_point
    max = len(puzzle)-1
    cmds = [[(0,  0),    (1,0),              (0,1)],
            [(max,0),    (-1,0),             (0,1)],
            [(0,0),     (0,1),               (1,0)],
            [(0,max),    (0,-1),             (1,0)]]

    for cmd in cmds:
        start_point = point = Vector(*cmd[0])
        checking_direction = Vector(*cmd[1])
        offs = Vector(*cmd[2])
        for _ in range(len(puzzle)):
            start_point = point.copy()
            puzzle[point.x][point.y].visible = True
            high = puzzle[point.x][point.y].high
            for _ in range(len(puzzle)-1):
                point.add(checking_direction)
                if high < puzzle[point.x][point.y].high:
                    puzzle[point.x][point.y].visible = True
                    high = puzzle[point.x][point.y].high
            point = start_point.copy()
            point.add(offs)

    n = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[1])):
            n += puzzle[i][j].visible
    return n

def solve2(puzzle):
    dirs = [Vector(1,0), Vector(0,1),Vector(-1,0),Vector(0,-1)]

    for x in range(1,len(puzzle)-1):
        for y in range(1,len(puzzle)-1):
            start_point = Vector(x,y)
            high = puzzle[start_point.x][start_point.y].high
            #print("Startpoint",start_point, "high", high)
            for dir in dirs:
                puzzle[start_point.x][start_point.y].score[dir] = 0
                next_point = start_point.copy()
                test = True
                while test:
                    next_point.add(dir)
                    if (min(next_point.x, next_point.y) < 0) or (max(next_point.x, next_point.y) >= len(puzzle)):
                        test = False
                    else:
                        #print("inc sore for", dir)
                        puzzle[start_point.x][start_point.y].score[dir] += 1
                        if high <= puzzle[next_point.x][next_point.y].high:
                            test = False
    
    global_score = 0
    for x in range(1,len(puzzle)-1):
        for y in range(1,len(puzzle)-1):
            global_score =  max(global_score, np.prod(list(puzzle[x][y].score.values())))

    return global_score

puzzle = read_puzzle('d08.txt')

print("Task 1", solve1(puzzle))
print("Task 2", solve2(puzzle))