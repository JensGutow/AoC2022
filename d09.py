# --- Day 9: Rope Bridge ---
import copy

def read_puzzle(file):
    return  [line.split(" ") for line  in open(file).read().strip().split("\n")] 

def make_move(t, h):
    dx = h[0] - t[0]
    dy = h[1] - t[1]
    DX = DY = 0
    if max(abs(dx), abs(dy)) > 1:
        if dx: DX = dx//abs(dx) 
        if dy: DY = dy//abs(dy)
    return [t[0] + DX, t[1] + DY]

def solve(puzzle, n ):
    Dir = {"R": (1,0), "L":(-1,0), "U":(0,1), "D":(0,-1)}
    visited = {} # (x,y):1
    ropes = [copy.deepcopy([0,0]) for _ in range(n)]
    for move in puzzle:
        d, n = move
        n = int(n)
        dx, dy = Dir[d]
        for _ in range(n):
            # ropes[0] is head -> ropes[n-1] is last tail
            ropes[0][0] += dx
            ropes[0][1] += dy
            for i in range(len(ropes)-1):
                ropes[i+1] = make_move(ropes[i+1], ropes[i])
            visited[tuple((ropes[i+1][0], ropes[i+1][1]))] = 1
    return sum(visited.values())    

puzzle = read_puzzle('d09.txt')

print("Task 1", solve(puzzle, 2))
print("Task 2", solve(puzzle, 10))