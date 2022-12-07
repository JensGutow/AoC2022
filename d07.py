# --- Day 7: No Space Left On Device ---

def read_puzzle(file):
     return [[info for info in round.split(" ")] for round in open(file).read().strip().split("\n")]

class Directory:
    root = None # static var
    def __init__(self,parent, name) -> None:
        self.parent = parent
        self.name = name
        self.dirs = {} # name: Directory(parent, name)
        self.files = [] # [(name, size),...]
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

def handle_command(dir:Directory, cmd, parms) -> Directory :
    if cmd == "cd":
        if parms[0] == "..":  return dir.parent            
        elif parms[0] == "/": return  Directory.root
        else: return  dir.dirs[parms[0]]
    else: return dir

def handle_file(dir:Directory, size, name):
    dir.files.append((name,int(size)))

def handle_dir(dir:Directory, dir_name):
    dir.dirs[dir_name] = Directory(dir, dir_name)

def get_filesize(dir: Directory):
    size = 0
    for file in dir.files:
        size += file[1]
    for d in dir.dirs.values():
        size += get_filesize(d)
    return size

def solve(puzzle):
    Directory.root = current_dir = root = Directory(None, "root")

    for line in puzzle:
        if line[0] == "$": 
            cmd = line[1]
            parms = [parm for parm in line[2:]]
            current_dir = handle_command(current_dir, cmd, parms)
        elif line[0] == "dir" : handle_dir(current_dir, line[1])
        else : handle_file(current_dir, line[0], line[1])
    
    root.size_update()

    d = {} # {dir_name: Directory()}

    # Task 1
    root.list_size(d)
    size_1 = 0 
    for s in d.values():
        if s < 100000:
            size_1+=s
    
    # Task 2
    unused_space = 70000000 - root.size
    to_delete  = 30000000 - unused_space 
    for size_2 in sorted(d.values()):
        if size_2 >= to_delete: break

    return size_1, size_2

puzzle = read_puzzle('d07.txt')

task1, task2 = solve(puzzle)

print("Task 1", task1)
print("Task 2", task2)