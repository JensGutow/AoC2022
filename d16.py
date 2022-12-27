# --- Day 16: Proboscidea Volcanium ---
import re
import functools

class Node():
    nodes = {}
    def __init__(self, line) -> None:
        letters = re.findall(r"[A-Z][A-Z]", line)
        self.rate =  int(re.findall(r"[0-9]+", line)[0])
        self.valve = letters[0]
        self.to = letters[1:]
        self.isOpen = self.rate == 0 # 0: Valve is damaged and opened
        Node.nodes[self.valve] = self
        #ValveStates.addNode(self)

    @staticmethod
    def getPressure(path):
        return sum([Node.nodes[node].rate for node in path.split(",") if Node.nodes[node].isOpen])

    @staticmethod
    def setValveStatus(path):
        for node in Node.nodes.keys():
            status = True if node in path.split(",") else False
            Node.nodes[node].isOpen = status

    @staticmethod
    def getValveStatus():
        valveStatus = 0
        for i, node in enumerate(Node.nodes.keys()):
            if Node.nodes[node].isOpen:
                valveStatus |= (1 << i)
        return valveStatus

class ValveStates():
    valveOpenState = 0   # BitIndex set <-> valve "XX" is open
    valveToStateInx = {} # "XX" : BitIndex
    pressure = 0

    @staticmethod
    def addNode(node : Node):
        if node.rate == 0: return # 0-valve shall not be added
        if node.valve in ValveStates.valveToStateInx.keys(): return # was added before already
        inx = 0 if not ValveStates.valveToStateInx else len(ValveStates.valveToStateInx) + 1
        ValveStates.valveToStateInx[node.valve] = inx

    @staticmethod
    def openValve(valve):
        if valve in ValveStates.valveToStateInx:
            ValveStates.valveOpenState |= (1 << ValveStates.valveToStateInx[valve])

    @staticmethod
    def closeValve(valve):
        if valve in ValveStates.valveToStateInx:
            ValveStates.valveOpenState &= ~(1 << ValveStates.valveToStateInx[valve])


    @staticmethod
    def setValveStatus(valve, open:bool):
        if open: ValveStates.openValve(valve)
        else: ValveStates.closeValve(valve)
            
    @staticmethod
    def getValveState():
        return ValveStates.valveOpenState

    @staticmethod
    def isValveOpen(valve):
        # damaged valves are not part of ValveStates and are open always
        if valve not in ValveStates.valveToStateInx: return True
        else: 
            inx = ValveStates.valveToStateInx[valve]
            return (ValveStates.valveOpenState & (1 << inx)) != 0

def read_puzzle(file):
    nodes =  [Node(line) for line in open(file).read().strip().split("\n") ]
    return nodes

N = 1000000
n = 0

@functools.cache
def getMaxPressure(start, maxPath, valveStatus, pressure, time):
    global N
    global n 
    n += 1
    if n%N==0:
        n=0
        print(time, maxPath)
    if not ValveStates.isValveOpen(start):
        ValveStates.openValve(start)

        time -= 1
        pressure + Node.nodes[start].rate
        if time == 0: return pressure
    time -= 1
    pressure + Node.nodes[start].rate
    if time == 0: return pressure

    assert time > 0

    maxPressure = 0
    for node in Node.nodes[start].to:
        valveState = ValveStates.getValveState()
        maxPath = maxPath +"," + node
        pressure = (Node.nodes[start].rate * time) + getMaxPressure(node, maxPath, ValveStates.getValveState(), ValveStates.pressure, time)
        maxPressure = max(maxPressure, pressure)
        ValveStates.valveOpenState = valveState
        maxPath = maxPath[:-3]
    return maxPressure

def heuristic(item):
    return item[PRESSURE]

NODE            = 0
PATH            = 1 # comma separated
PRESSURE        = 2
TIME            = 3
VALVE_STATUS    = 4

def bfs(start, pressure, time):
    queue = []
    queue.append([start,start, pressure, time, 0])
    while time:
        time -= 1
        if len(queue) > 500: 
            queue = sorted(queue, key=heuristic, reverse=True)[:500]
        nextQueue = []
        while queue:
            item = queue.pop()
            Node.setValveStatus(item[PATH])
            pressure = Node.getPressure(item[PATH]) + item[PRESSURE]
            for node in Node.nodes[item[NODE]].to:
                nodeWasOpen = Node.nodes[node].isOpen
                Node.nodes[node].isOpen = True
                valveStatus = Node.getValveStatus()
                nextQueue.append([node, item[PATH] +"," + node, pressure, time, valveStatus])
                Node.nodes[node].isOpen = nodeWasOpen
        queue = nextQueue

    return sorted(queue, key=heuristic, reverse=True)[0][PRESSURE]



def solve1(puzzle):
    return bfs("AA", 0, 30)

puzzle = read_puzzle('d16.txt')

print("Task 1", solve1(puzzle))
#print("Task 2", solve1(puzzle))