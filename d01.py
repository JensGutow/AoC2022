def read_puzzle(file):
    return [[int(cal) for cal in elfe.split("\n") ] for elfe in open(file).read().strip().split("\n\n")]

def löse(puzzle, n):
    return sum(sorted([sum(elf) for elf in puzzle], reverse=True)[0:n])
        
puzzle = read_puzzle('d01.txt')

print(f"Task1: {löse(puzzle, 1)}")
print(f"Task1: {löse(puzzle, 3)}")