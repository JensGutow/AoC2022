# --- Day 10: Cathode-Ray Tube ---

class Crt:
    def __init__(self, regx:int) -> None:
        self.screen = []
        self.pos = 0
        self.sprite = []
        self.update_sprite_pos(regx)

    def update_screen(self):
        c = "#" if (self.pos%40) in self.sprite else " "
        self.screen.append(c)
        self.pos += 1

    def update_sprite_pos(self, pos:int):
        self.sprite = [i for i in range(pos-1,pos+2)]

    def print_screen(self):
        assert len(self.screen) >= 240
        s = "".join(self.screen)
        pos = 0
        print(" ---------- CRT -----------")
        while pos < 240:
            print(s[pos:pos+40])
            pos+=40

class Cpu:
    def __init__(self) -> None:
        self.reg_x = 1
        self.cycle = 0
        self.th_i = 0
        self.th = [20 + (i*40)  for i in range(6)]
        self.signal_values = []
        self.signal_strength =  []
        self.crt = Crt(self.reg_x)

    def handle_cmd(self, cmd):
        if cmd[0] == "noop": self.noop()
        else: self.addx(int(cmd[1]))

    def noop(self):
        self.cycle += 1
        self.update_signal_strength()
        self.crt.update_screen()

    def addx(self, x:int):
        self.cycle += 2
        self.crt.update_screen()
        self.crt.update_screen()
        self.update_signal_strength()
        self.reg_x += x
        self.crt.update_sprite_pos(self.reg_x)

    def update_signal_strength(self):
        if self.th_i < len(self.th) and self.cycle >= self.th[self.th_i]:
            self.signal_values.append(self.reg_x)
            self.signal_strength.append(self.reg_x * self.th[self.th_i])
            self.th_i += 1

def read_puzzle(file):
    return [line.split(" ") for line in open(file).read().strip().split("\n")]

cpu = Cpu()
def solve(puzzle):
    for cmd in puzzle:
        cpu.handle_cmd(cmd)

    cpu.crt.print_screen()
    return sum(cpu.signal_strength)

puzzle = read_puzzle('d10.txt')

print("Task 1", solve(puzzle))

'''
---------- CRT -----------
#### #### ###  #### #  #  ##  #  # ###  
   # #    #  # #    #  # #  # #  # #  # 
  #  ###  ###  ###  #### #    #  # #  # 
 #   #    #  # #    #  # # ## #  # ###  
#    #    #  # #    #  # #  # #  # #
#### #    ###  #    #  #  ###  ##  #

ZFBFHGUP

Task 1 15680
'''