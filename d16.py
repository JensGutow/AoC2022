# --- Day 16: Proboscidea Volcanium ---
import re

class Node():
    nodes = {}
    rate = 0
    def __init__(self, line) -> None:
        letters = re.findall(r"[A-Z][A-Z]", line)
        self.rate =  int(re.findall(r"[0-9]+", line)[0])
        self.valve = letters[0]
        self.to = letters[1:]
        self.predecessor = None
        self.closed = self.rate != 0 # 0: Valve is damaged and opened
        Node.nodes[self.valve] = self

    def step(self, time, rate):
        time += 1
        if self.closed:
            self.closed = False
            time += 1
        rate += self.rate
        return time, rate

def FloydWarshallWithPathReconstruction(A, V, E):
    # https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
    # array of minimum distances, init with infinity
    dist = {edge:9E99 for edge in E}
    # array of vertexes, init with null
    next = {}

    for edge in E:
        dist[edge] = -A[edge] # The weight of the edge (u, v)
        next[edge] = edge[1] # the End node of the edge
    for vertex in V:
        dist[(vertex, vertex)] = 0 # diagonal -> 0
        next[(vertex, vertex)] = vertex
    # standard Floyd-Warshall implementation
    for k in V:
        for i in V:
            if (i,k) not in dist: continue
            for j in V:
                #if i==j : continue
                #if i==k : continue
                #if k==j : continue
                if (i,j) not in dist: continue
                if (k,j) not in dist: continue

                if dist[(i,j)] > dist[(i,k)] + dist[(k,j)]:
                    dist[(i,j)] = dist[(i,k)] + dist[(k,j)]
                    next[(i,j)] = next[(i,k)]
                if ((dist[(i,j)]) < (-100)):
                    print(i,j, dist[(i,j)])
    return dist, next

def  getPath(u, v, dist, next):
    if not (u,v) in next: return []
    path = [u]
    while u != v:
        u = next[(u,v)]
        path.append(u)
    return path

def read_puzzle(file):
    nodes =  [Node(line) for line in open(file).read().strip().split("\n") ]
    return nodes

def network_sim(start:Node, time:int, rate:int, maxRate:list):
    if time >=25: 
        maxRate[0] = max(maxRate[0], rate)
        return

    time, rate = start.step(time, rate)
    for node in start.to:
        network_sim(Node.nodes[node], time, rate, maxRate)
        
def purgeMatrix(nodes):
    for node in nodes:
        destinations = set(node.to)
        source = {n2.valve for n2 in nodes if node.valve in n2.to}
        canPurge =  len(source.intersection(set(destinations))) == 0
        print("node ", node.valve,  " canPurge:", canPurge, "source:",source, " des:", destinations)


def solve1(puzzle):
#     # Adjacency matrix: items ("AA","BB"):rate
#     A = {(node.valve,to):node.rate for node in puzzle for to in node.to}
#     # Vertexes: items: "AA", ..., 
#     V = {node.valve for node in puzzle}
#     # Edges: items: ("AA","DD"),...: edge from "AA" to "DD" exist
#     E = set(A.keys())
    
#     Dist, Next = FloydWarshallWithPathReconstruction(A, V, E)

#     print(len(Dist))
#     l = 0
#     for k,v in Dist.items():
#         if v != 0:
#             l += 1
#             print(k,v)
#     print(l)
#     print(len(V))

#     for v in V:
#         path = getPath("AA", v, Dist, Next)
#         print("path from ", "AA", " to ", v," : ", path)'
#    purgeMatrix(puzzle)


    ValveZero = [n for n in puzzle if n.rate == 0]
    l1 = len(puzzle) - len(ValveZero)
    print(len(puzzle), len(ValveZero), l1, 2**l1)
    return 0

puzzle = read_puzzle('d16.txt')

print("Task 1", solve1(puzzle))
#print("Task 2", solve1(puzzle))