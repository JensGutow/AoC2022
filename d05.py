from collections import defaultdict
import re 

# --- Day 5: Supply Stacks ---
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2

def create_stapel(data):
    d = defaultdict(list)
    for line in data:
        for m in re.finditer(r"[A-Z]", line):
                index = (m.start()-1)//4
                d[index].append(line[m.start()])
    for _, value in d.items():
        value.reverse()

    stapel = []    
    for i in range(len(d)):
        stapel.append(d[i])
    
    return stapel

def read_puzzle(file):
    data_ =  [ parts.split("\n") for parts in open(file).read().split("\n\n") ]
    stapel = create_stapel(data_[0])

    data = [d.split(" ")  for d in data_[1]]
    d_ = []
    for a,b,c,d,e,f in data:
        d_.append((int(b),int(d),int(f)))

    return d_, stapel

def solve1(puzzle, stapel_):
    for n, von, zu in puzzle:
        for _ in range(n):
            item = stapel_[von-1].pop()
            stapel_[zu-1].append(item)
    result = "".join([s[-1] for s in stapel_])
    return(result)
    
def solve2(puzzle, stapel_):
    for n, von, zu in puzzle:
        temp = []
        for _ in range(n):
            item = stapel_[von-1].pop()
            temp.append(item)
        temp.reverse()
        for item in temp:
            stapel_[zu-1].append(item)

    result = "".join([s[-1] for s in stapel_])
    return(result)

puzzle, stapel = read_puzzle('d05.txt')
s = [s.copy() for s in stapel]

print(solve1(puzzle, s))
print(solve2(puzzle, stapel))