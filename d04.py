# --- Day 4: Camp Cleanup ---

def read_puzzle(file):
    return [[list(map(int,s.split("-"))) for s in section.split(",")] for section in open(file).read().strip().split("\n") ]

def is_fully_area(p1, p2):
    check = lambda a, b: a[0] >= b[0] and a[1] <= b[1]
    return check(p1, p2) or check(p2,p1)

def is_partly_area(p1, p2):
    check = lambda a, b: b[0] <= a[1] and b[1] >= a[0]
    return check(p1, p2) or check(p2,p1)

def solve(puzzle):
    c1, c2 = 0, 0
    for g1, g2 in puzzle:
        c1 += is_fully_area(g1, g2)
        c2 += is_partly_area(g1, g2)
    return c1, c2

puzzle = read_puzzle('d04.txt')

print(puzzle)
results = solve(puzzle)

print(f"Task1: {results[0]}")
print(f"Task2: {results[1]}")