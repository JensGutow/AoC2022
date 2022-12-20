# --- Day 17: Pyroclastic Flow ---
import copy
def read_puzzle(file):
    return [(-1,0) if c == "<" else (1,0) for c in open(file).read().strip()]

class Item():
    def __init__(self, items:set) -> None:
        self.item = items

    def setItem(self, item:set):
        self.item = item

    def xmin(self):
        return min([item[0] for item in self.item])

    def xmax(self):
        return max([item[0] for item in self.item])

    def high(self):
        return max([item[1] for item in self.item])

    def ymin(self):
        return min([item[1] for item in self.item])

    def move(self, dir, returnCopy = False):
        item = set()
        for coord in self.item:
            point = [0,0]
            point[0] = coord[0] + dir[0]
            point[1] = coord[1] + dir[1]
            item.add(tuple(point))
        if returnCopy:
            return Item(item)
        else:
            self.item = item

    def hasCollision(self, s):
        return len(self.item.intersection(s.item)) > 0

    def insertItem(self, item):
        self.item = self.item.union(item.item)

    def print(self):
        ymax = self.high()
        ymin = self.ymin()
        for y in range(ymax, ymin-1, -1):
            line = ""
            for x in range(0, 8):
                c = "#" if (x,y) in self.item else "."
                line += c
            print(line)



MINUS   = Item({(0,0), (1,0),(2,0),(3,0)}) 
PLUS    = Item({(1,0), (0,-1),(1,-1),(2,-1),(1,-2)}) 
L       = Item({(2,0), (2,-1),(0,-2),(1,-2),(2,-2)}) 
I       = Item({(0,0), (0,-1),(0,-2),(0,-3)}) 
QUADRAT = Item({(0,0), (1,0),(0,-1),(1,-1)}) 
ITEMS = [MINUS, PLUS, L, I, QUADRAT]

def solve1(puzzle):
    ROCK = Item({(0,0)})
    dir_index = 0
    for i in range(2022):
        
        item = copy.deepcopy(ITEMS[i%len(ITEMS)])
        h = ROCK.high()
        if i%1000==0:
            print("item", i, " high", h)
        item.move((3, h + 4 - item.ymin()))
        while True:
            dir = puzzle[dir_index]
            dir_index = (dir_index + 1) % len(puzzle)
            item_c = item.move(dir, True)
            if (item_c.xmin() > 0) and ((item_c.xmax()) < 8) and not ROCK.hasCollision(item_c):
                item.setItem(item_c.item)
            item2 = copy.deepcopy(item)
            item2.move((0,-1))
            if ROCK.hasCollision(item2) or (item2.high() <= 0):
                assert not ROCK.hasCollision(item)
                ROCK.insertItem(item)
                break
            else:
                item = item2
    return ROCK.high()

puzzle = read_puzzle('d17.txt')


print("Task 1", solve1(puzzle))
#print("Task 2", solve1(puzzle))