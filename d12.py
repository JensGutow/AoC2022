# --- Day 12: Hill Climbing Algorithm  -> A* Algorithm ---
import queue as Q

DIR = [[1,0],[-1,0],[0,1],[0,-1]]

class Node():
    def __init__(self,high, coords) -> None:
        self.cost = 10000000
        self.predecessor = None
        self.high = high
        self.coords = coords

    def __cmp__(self, other):
        return other.cost >  self.cost

    def __lt__(self, other):
        return other.cost >  self.cost


def read_puzzle(file):
    START = None
    ZIEL = None
    nodes = {}
    start_set = set()
    for i, line in enumerate(open(file).read().split("\n") ):
        for j, c in enumerate(line):
            
            h = ord(c)
            if c == "S": h = ord("a")
            elif c == "E": h = ord("z")
            node = Node(h - ord("a"), (i,j))
            nodes[(i,j)] =  node
            if c == "S" : 
                START = node
                start_set.add(node)
            if c == "E" : ZIEL = node
            if c == "a": start_set.add(node)

    return  START, ZIEL, nodes, start_set


def solve(puzzle):
    START, ZIEL, nodes, start_set = puzzle
    part_1_n =  find_shortest_path(START, ZIEL, nodes)
    part_2_n = sorted([find_shortest_path(item, ZIEL, nodes) for item in start_set])[0]
    return part_1_n, part_2_n

def find_shortest_path(START, ZIEL, nodes)    :
    openList  = Q.PriorityQueue()
    START.cost = 0
    openList.put(START)
    openList2 = set()
    openList2.add(START)
    closedList = set()
    
    endFound = False
    while not openList.empty():
        node = openList.get()
        openList2.remove(node)
        if node == ZIEL: 
            endFound = True
            break

        closedList.add(node)

        for dir in DIR:
            next = (node.coords[0] + dir[0], node.coords[1] + dir[1])
            if not next in nodes: continue
            next = nodes[next]
            if next in closedList: continue
            dh = next.high - node.high
            if dh > 1: continue
            curr_cost = node.cost  +  abs(ZIEL.coords[0] - next.coords[0]) + abs(ZIEL.coords[1] - next.coords[1])
            if next in openList2 and curr_cost >= next.cost: continue
            if next not in openList2:
                next.cost = curr_cost
                next.predecessor = node
                openList.put(next)
                openList2.add(next)
            elif  (curr_cost < next.cost):
                next.cost = curr_cost
                next.predecessor = node
    
    n = 0
    if endFound:
        node = ZIEL
        while node != START:
            node = node.predecessor
            n += 1
    else:
        n = 100000000000
    return n

puzzle = read_puzzle('d12.txt')

print(solve(puzzle))
