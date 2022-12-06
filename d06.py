# --- Day 6: Tuning Trouble ---

from collections import Counter

def read_puzzle(file):
    return open(file).read() 

def solve1(puzzle, n):
    cnt = Counter()

    for char in puzzle:
        cnt[char] = 1

    for i in range(n,len(puzzle)):
        found = True
        if len(set(puzzle[i-n:i])) < n : continue
        for j in range(i-n, i):
            if cnt[puzzle[j]] > 1:
                found = False
        if found: break
    return i

puzzle = read_puzzle('d06.txt')

print("Task 1", solve1(puzzle,4))
print("Task 2", solve1(puzzle,14))