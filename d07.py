# --- Day 7: No Space Left On Device ---
import sys # recusion limit

sys.setrecursionlimit(10000) 
def read_puzzle(file):
     return [[info for info in round.split(" ")] for round in open(file).read().strip().split("\n")]

class Directory:
    def __init__(self,parent, name) -> None:
        self.parent = parent
        self.name = name
        self.dirs = {} # name: Directory(parent, name)
        self.files = []
        self.size = 0
    
    def size_update(self):
        for dir in self.dirs.values():
            dir.size_update()
        
        self.size = 0
        for file in self.files:
            self.size += file[1]
        for dir in self.dirs.values():
            self.size += dir.size

    def list_size(self, d):
        d[self] = self.size
        for dir in self.dirs.values():
            dir.list_size(d)

root = None

def handle_command(dir:Directory, cmd, parms) -> Directory :
    #print (f"handle_command: cmd: {cmd} parms: {parms}")
    if cmd == "cd":
        if parms[0] == "..":  return dir.parent            
        elif parms[0] == "/": return  root
        else: return  dir.dirs[parms[0]]
    else: return dir

def handle_file(dir:Directory, size, name):
    #print (f"handle_file: size: {size} name: {name}")
    dir.files.append((name,int(size)))

def handle_dir(dir:Directory, dir_name):
    #print (f"handle_dir: dir:{dir.name} dir_name: {dir_name} ")

    if not dir_name in dir.dirs:
        d = Directory(dir, dir_name)
        dir.dirs[dir_name] = d

def get_filesize(dir: Directory):
    size = 0
    for file in dir.files:
        size += file[1]
    for d in dir.dirs.values():
        size += get_filesize(d)
    return size

def solve(puzzle):
    global root
    
    root = Directory(None, "root")
    current_dir = root

    for line in puzzle:
        #print("...solve", line)
        if line[0] == "$": 
            cmd = line[1]
            parms = [parm for parm in line[2:]]
            current_dir = handle_command(current_dir, cmd, parms)
        elif line[0] == "dir" : handle_dir(current_dir, line[1])
        else : handle_file(current_dir, line[0], line[1])
    
    root.size_update()

    d = {}
    root.list_size(d)
    size = 0 
    for s in d.values():
        if s < 100000:
            size+=s
    
    unused_space = 70000000 - root.size
    to_delete  = 30000000 - unused_space 
    for v in sorted(d.values()):
        if v > to_delete: break

    return size, v

puzzle = read_puzzle('d07.txt')

print(solve(puzzle))



#print("Task 1", solve1(puzzle))
#print("Task 2", solve1(puzzle))