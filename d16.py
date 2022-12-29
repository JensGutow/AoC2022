# --- Day 16: Proboscidea Volcanium ---
import re
import copy

class Node():
    nodes = {}
    def __init__(self, line) -> None:
        letters = re.findall(r"[A-Z][A-Z]", line)
        self.rate =  int(re.findall(r"[0-9]+", line)[0])
        self.valve = letters[0]
        self.to = letters[1:]
        self.isOpen = self.rate == 0 # 0: Valve is damaged and opened
        Node.nodes[self.valve] = self

    @staticmethod
    def getPressure(valveState):
        pressure = 0
        for node in Node.nodes.keys():
            if valveState[node]:
                pressure += Node.nodes[node].rate
        return pressure

    @staticmethod
    def valveIsOpen(node, valveState):
        return valveState[node] 
    
def read_puzzle(file):
    nodes =  [Node(line) for line in open(file).read().strip().split("\n") ]
    return nodes

def heuristic(item):
    return (item[PRESSURE])


NODE_MY         = 0
NODE_ELEPHANT   = 1
PRESSURE        = 2
PATH            = 3 # comma separated nodes
VALVE_STATE     = 4

MAX_N           = 10000

def compressQueue(q, n):
    if len(q) > n: 
        q = sorted(q, key=heuristic, reverse=True)
        return q[:n]
    else: 
        return q

def step(queue, player, updatePressure = True):
    queue = compressQueue(queue, MAX_N)
    nextQueue = []
    while queue: 
        item = queue.pop(0)
        valveStates = copy.deepcopy(item[VALVE_STATE])
        pressure = item[PRESSURE]
        if updatePressure:
            pressure +=  Node.getPressure(valveStates)
        if all([v for v in item[VALVE_STATE].values()]): 
            # whenn all valves are open -> only update the current item but do not insert new items
            item[PRESSURE] = pressure
            nextQueue.append(item)
            continue

        # if a node can be open -> open it
        if not Node.valveIsOpen(item[player], valveStates):
            valveStates2 = copy.deepcopy(valveStates)
            valveStates2[item[player]] = True
            nextQueue.append([item[NODE_MY], item[NODE_ELEPHANT], pressure, item[PATH] + "," + item[player], valveStates2])
        # check all next valves
        for node in Node.nodes[item[player]].to:
            if player == NODE_ELEPHANT:
                node_my         = item[NODE_MY]
                node_elephant   = node
            else:
                node_my         = node
                node_elephant   = item[NODE_ELEPHANT]        
            nextQueue.append([node_my, node_elephant, pressure, item[PATH] + "," + node, valveStates])
    return nextQueue

def bfs(start, pressure, time, part1):
    valveState = {key : valve.rate == 0 for key, valve in Node.nodes.items()}

    queue = []
    queue.append([start,start, pressure, "AA", valveState])
    while time:
        print(time)
        time -= 1
        queue = step(queue, NODE_MY, updatePressure=True)
        if not part1:
            queue = step(queue, NODE_ELEPHANT, updatePressure=False)        

    queue = sorted(queue, key=heuristic, reverse=True)
    return queue[0][PRESSURE]

def solve1(puzzle):
    return bfs("AA", 0, 30, part1=True)

def solve2(puzzle):
    return bfs("AA", 0, 26, part1=False)

puzzle = read_puzzle('d16.txt')

print("Task 1", solve1(puzzle))
print("Task 2", solve2(puzzle))