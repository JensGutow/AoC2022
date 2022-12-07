# --- Day 6: Tuning Trouble ---

def read_puzzle(file):
    return open(file).read() 

def solve1(puzzle, n):
    for i in range(n,len(puzzle)):
        if len(set(puzzle[i-n:i])) < n : continue
        break
    return i

puzzle = read_puzzle('d06.txt')

print("Task 1", solve1(puzzle,4))
print("Task 2", solve1(puzzle,14))