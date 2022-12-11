# --- Day 11: Monkey in the Middle ---
import re
import copy

class Monkey():
    monkeys = None
    max_teiler = None
    task1 = True

    def __init__(self, s) -> None:
        self.nr = int(re.findall(r"[\d]+", s[0])[0])
        self.items = list(map(int,re.findall(r"[\d]+", s[1])))
        self.op = "MULT" if "*" in s[2] else "ADD"
        self.operand = s[2].split(" ")[-1]
        self.teiler = int(s[3].split(" ")[-1])
        self.throw_true = int(s[4].split(" ")[-1])
        self.throw_false = int(s[5].split(" ")[-1])
        self.number_inspect_items = 0

    def throw(self, item):
        self.items.append(item)

    def inspect_items(self):
        self.number_inspect_items += len(self.items)
        while self.items:
            a = self.items.pop(0)
            b = a if self.operand == "old" else int(self.operand)
            c = a + b if self.op == "ADD" else a * b
            w_level =  c // 3 if self.task1 else c
            # Einschaenkung des Ergebnissses auf das Produkt der Teiler aller Affen
            # max_teiler = produkt aller teiler aller Affen, diese sind alle Primzahlen
            # ==> x % teiler <==> (x % max_teiler) % teiler
            w_level = w_level % self.max_teiler
            thrown_to = self.throw_true if w_level % self.teiler == 0 else self.throw_false
            self.monkeys[thrown_to].throw(w_level)

def read_puzzle(file):
    return [Monkey(ds.split("\n")) for ds in open(file).read().split("\n\n")]

def solve(monkeys, task1):
    Monkey.monkeys = monkeys
    Monkey.task1 = task1

    max_teiler = 1
    for monkey in monkeys:
        max_teiler *= monkey.teiler
    Monkey.max_teiler = max_teiler
    
    n = 20 if task1 else 10000
    for _ in range(n):
        for monkey in monkeys:
            monkey.inspect_items()

    n = sorted([m.number_inspect_items for m in monkeys],reverse=True)
    
    return n[0] * n[1]

puzzle = read_puzzle('d11.txt')

puzzle1 = copy.deepcopy(puzzle)
print("Task 1", solve(puzzle1, True))
print("Task 2", solve(puzzle, False))