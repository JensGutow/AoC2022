# --- Day 4: Camp Cleanup ---

def read_puzzle(file):
    return [list(map(int,s.split("-"))) for section in open(file).read().strip().split("\n") for s in section.split(",")]

def is_fully_area(p1, p2):
    check = lambda a, b: a[0] >= b[0] and a[1] <= b[1]
    return check(p1, p2) or check(p2,p1)

def is_partly_area(p1, p2):
    check = lambda a, b: b[0] <= a[1] and b[1] >= a[0]
    return check(p1, p2) or check(p2,p1)

def solve(puzzle):
    c1, c2 = 0, 0
    for i in range(len(puzzle)//2):
        g1, g2 = puzzle[2*i], puzzle[2*i+1]
        c1 += is_fully_area(g1, g2)
        c2 += is_partly_area(g1, g2)
    return c1, c2

puzzle = read_puzzle('d04.txt')

results = solve(puzzle)

print(f"Task1: {results[0]}")
print(f"Task2: {results[1]}")